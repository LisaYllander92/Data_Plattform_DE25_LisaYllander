from fastapi import FastAPI, status
from psycopg_pool import ConnectionPool
from psycopg.types.json import Json     # Convert Pydantic -> JSON
from psycopg import Connection          # Open Temporary Connection

from postgresql_fastapi.schema.product import ProductSchema


# Första blocket sätter upp grunden för applikationen
DATABASE_URL = "postgresql://postgres:bettan123@localhost:5432/lektion_5" #postgresql://USERNAME:PASSWORD@ADRESS:PORT/DB_NAME
pool = ConnectionPool(DATABASE_URL)
app = FastAPI(title="postgresql_fastapi")
"""
- DATABASE_URL: En "vägbeskrivning" till din databas som innehåller användarnamn, lösenord, plats (localhost) och databasnamnet lektion_5.
- pool: Istället för att öppna och stänga en ny anslutning för varje användare, skapar vi en Connection Pool. 
  Det är som en samling färdiga anslutningar som ligger och väntar, vilket gör appen mycket snabbare.
- app: Här skapar vi själva FastAPI-instansen som är motorn i din webbserver.
"""
@app.get("/")
def root() -> dict:
    return {"Hello": "World"}

# Det här blocket hanterar läsning från databasen.
@app.get("/products")
def get_products():
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT product FROM products_raw")
            rows = cur.fetchall()
    # rows = [(product_dict,), (product_dict,), ...]
    return [row[0] for row in rows]

"""
- with pool.connection(): Vi lånar en anslutning från poolen.
- with conn.cursor(): En "cursor" (markör) är det objekt som faktiskt pratar med databasen och håller i resultatet.
- cur.execute(...): Vi skickar ett SQL-kommando för att hämta all data i kolumnen product.
- cur.fetchall(): Vi tömmer markören på allt innehåll och sparar det i variabeln rows. 
  Det kommer ut som en lista av tupler, t.ex. [ (data1,), (data2,) ].
- List comprehension: [row[0] for row in rows] plockar ut det första värdet i varje tuple,
  så att användaren får en ren lista med JSON-objekt istället för krångliga tupler."""


@app.post(
    "/products",
    status_code=status.HTTP_201_CREATED,    # Swagger Documentation clarity
    response_model=ProductSchema,           # Swagger Documentation update
)

# Det här blocket tar emot ny data och ser till att den sparas säkert.
def post_product(product: ProductSchema) -> ProductSchema:
    # Query-Insert
    with pool.connection() as conn:
        with conn.transaction(): # all or nothing
            insert_product(conn, product)

    return product
"""
- product: ProductSchema: FastAPI läser in JSON-datan från användaren och kollar automatiskt mot ditt schema så att allt är korrekt ifyllt (validering).
- with conn.transaction(): Detta skapar en transaktion. Det betyder "allt eller inget". 
Om något går fel under sparandet rullas allt tillbaka så att databasen inte blir korrupt.
- insert_product(...): Vi anropar vår hjälpfunktion för att utföra själva sparandet."""

# Helper Method for DB-Queries
# Här sker den faktiska omvandlingen från Python till databasspråk.
def insert_product(conn: Connection, product: ProductSchema):
    conn.execute(
        "INSERT INTO products_raw (product) VALUES (%s)",
        (Json(product.model_dump()),)    # Note: Model_dump() konverterar schemat till dict
                                         # Json() kovenerterar till json(b)
    )
"""
- product.model_dump(): Gör om Pydantic-objektet till en vanlig Python-dictionary.
- Json(...): Omvandlar dictionaryn till det JSONB-format som PostgreSQL vill ha.
- %s och tuplen: Vi använder %s som en platshållare. Den sista kommatecknet i (Json(...),) är viktigt
 för att berätta för Python att detta är en tuple, vilket är vad execute förväntar sig.
"""