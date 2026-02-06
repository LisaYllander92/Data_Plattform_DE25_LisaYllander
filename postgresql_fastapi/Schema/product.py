from typing import Union
from pydantic import BaseModel

# Task 2 from lecture 5
class DimensionsSchema(BaseModel):
    width_cm: float
    height_cm: float
    depth_cm: float

class ProductSchema(BaseModel):
    product_id: str
    name: str
    price: float
    currency: str # SEK, USD, EUR
    category: Union[str, None]
    brand: Union[str, None] # from typing import Union
    tags: Union[list[str], None] = None # Task 1 from lecture 5
    dimensions: Union[DimensionsSchema, None] = None


