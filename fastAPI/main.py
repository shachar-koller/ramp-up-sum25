from fastapi import FastAPI, HTTPException
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


@app.delete("/items")
async def delete_item(item: Item):
    name = item.name
    if name in items:
        items.remove(name)
    else:
        # Raise HTTPException with status code for "not found"
        raise HTTPException(status_code=404, detail="Item not found.")
    return {}