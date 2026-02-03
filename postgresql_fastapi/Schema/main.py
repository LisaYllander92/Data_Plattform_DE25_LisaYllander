from fastapi import FastAPI, status
from psycopg_pool import ConnectionPool
from psycopg.types.json import Json     # convert Pydantc back to json
from psycopg import Connection          # Open temporary connection (automatic closing)

from schema.product import ProductSchema

DATABASE_URL = "postgresql://postgres:benny123@localhost:5432/lektion_5"
pool = ConnectionPool(DATABASE_URL)
app = FastAPI(title="lektion_5_postgresql_fastapi")

app = FastAPI(title="lektion_5_postgresql:fastapi")

@app.get("/")
def root() -> dict:
    return {"Hello": "World"}

@app.post(
    "/products",
    status_code=status.HTTP_201_CREATED, #Swagger Documentation clarity
    response_model=ProductSchema, #Swagger Documentation update
)
def post_product(product: ProductSchema) -> ProductSchema:


# Query-Insert
with pool.connection() as conn:
    insert_product(conn, product)
    conn.commit()  # Execute Logic (close connection when done)

    return product

# Helper Method for DB-Queries
def insert_product(conn: Connection, product: ProductSchema):
    conn.execute(
        "INSERT INTO products_raw(product) VALUES(%s)",
        (Json(product),)
    )