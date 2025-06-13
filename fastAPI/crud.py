from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# define model Item
class Item(BaseModel):
    name: str
    quantity: Optional[int] = 0

app = FastAPI()

items = {}


@app.post("/items")
def create(item: Item):
    name = item.name
    if name in items:
        raise HTTPException(status_code=409, detail="Item exists")
    items[name] = item
    return {"message": f"Added {name} to items."}
  
@app.get("/items")
def read(name: str):
    if name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[name]  
  
@app.put("/items")
def update(item: Item):
    name = item.name
    if name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[name] = item
    return {"message": f"Updated {name}."}
  
@app.delete("/items")
def delete(item: Item):
    name = item.name
    if name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[name]
    return {"message": f"Deleted {name}."}



# commands to use:

# 1.
# curl -X POST \
#   -H 'Content-Type: application/json' \
#   -d '{"name": "rock"}' \
#   http://localhost:8000/items

# 2.
# curl http://localhost:8000/items?name=rock

# 3. 
# curl -X PUT \
#   -H 'Content-Type: application/json' \
#   -d '{"name": "rock", "quantity": 100}' \
#   http://localhost:8000/items

# 4.
# curl -X DELETE \
#   -H 'Content-Type: application/json' \
#   -d '{"name": "rock"}' \
#   http://localhost:8000/items

# 5.
# curl http://localhost:8000/items?name=rock