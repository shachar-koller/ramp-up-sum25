from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

books = []

# Basic model
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

@app.post("/books")
async def create_book(book: Book):
    books.append(book)
    return book

@app.get("/books")
async def get_books():
    return books

@app.get("/books/{id}")
async def get_book(id: int):
    for book in books:
        if book.id == id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{id}")
async def update_book(id: int, title: str, author: str, year: int):
    for book in books:
        if book.id == id:
            book.title = title
            book.author = author
            book.year = year
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{id}")
async def delete_book(id: int):
    for book in books:
        if book.id == id:
            books.remove(book)
            return {"message": f"Book {id} deleted"}
    raise HTTPException(status_code=404, detail="Book not found")