import requests
from typing import Union

from fastapi import FastAPI, status

from schema.user import UserSchemaResponse
from schema.user import UserSchema
from schema.fox import FoxSchema

userList: list[UserSchema] = [
    UserSchema(username="John", password="123"),
    UserSchema(username="Frida", password="124"),
    UserSchema(username="Tommy", password="125")
]
app = FastAPI(title="My First API APP")

@app.get("/")
def root():
    return {"Hello": "World"} # dictionary "key:value" pairs

# https://www.google.se/search?q=bananas&


# two endpoints - "items" and "item_id"
# Example ordering cloths online
@app.get("/items/{item_id}") #{item_is} is dynamic. Try: localhost:8000/items/248?color=black
def get_item(item_id: int, color: Union[str, None] = None): # default value = None
    return {"item_id": item_id, "color": color}

@app.get("/users", response_model=list[UserSchemaResponse])
def get_users() -> list[UserSchemaResponse]: # what type we expect to receive
    return userList

@app.post(
    "/users",
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED
)

def post_user(user: UserSchema) -> UserSchema: # Body
    userList.append(user)
    return user

@app.get("/fox", response_model=FoxSchema)
def get_fox() -> FoxSchema:
    response = requests.get("https://randomfox.ca/floof/")
    result_json =response.json()

    fox = FoxSchema(**result_json) # convert JSON -> Python Object

    #print(f"DEBUGGING {result_json}")
    return fox