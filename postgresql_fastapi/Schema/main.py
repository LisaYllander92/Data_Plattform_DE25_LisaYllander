from fastapi import FastAPI, status

from postgresql_fastapi.Schema.product import ProductSchema

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
    return product
