from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Book Catalog API")


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


class Book(BookCreate):
    id: int


books: list[Book] = [
    Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
    Book(id=2, title="Pride and Prejudice", author="Jane Austen"),
]
