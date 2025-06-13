from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Depends

#Create the fastAPI object
app = FastAPI()



#Get
@app.get("/")
def read_root():
    return {"message": "Hello API"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

#Post
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}

def get_token():
    return "fake-token"

@app.get("/protected")
def protected(token: str = Depends(get_token)):
    return {"token": token}

from fastapi import HTTPException

@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id}

