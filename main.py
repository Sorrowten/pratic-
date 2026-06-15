from fastapi import FastAPI

app = FastAPI(title="Book Store API")

books = [
    {
        "id": 1,
        "title": "Война и мир",
        "author": "Л.Н. Толстой",
        "price": 950
    },
    {
        "id": 2,
        "title": "Преступление и наказание",
        "author": "Ф.М. Достоевский",
        "price": 870
    }
]

@app.get("/")
def home():
    return {"message": "Book Store API"}

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}

@app.post("/books")
def add_book(book: dict):
    books.append(book)
    return {"message": "Book added"}