"""
FastAPI REST API Starter Code
Building a Book Management API

Instructions:
1. Install required packages: pip install fastapi uvicorn
2. Complete the TODO sections below
3. Run with: uvicorn starter-code:app --reload
4. Visit http://127.0.0.1:8000/docs to see interactive API documentation
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

# TODO: Create FastAPI application instance
app = FastAPI(
    title="Book Management API",
    description="A simple REST API for managing a book collection",
    version="1.0.0"
)

# TODO: Create a Pydantic model for Book
# The model should have: id (int), title (str), author (str), year (int), genre (str)
class Book(BaseModel):
    pass  # Replace with your implementation


# In-memory database (list of books)
books_db = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Fiction"},
    {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949, "genre": "Dystopian"},
    {"id": 3, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813, "genre": "Romance"}
]


# TODO: Implement GET endpoint at root path "/" 
# Should return a welcome message
@app.get("/")
def read_root():
    pass  # Replace with your implementation


# TODO: Implement GET endpoint to retrieve all books
# Path: "/books"
# Should return the list of all books


# TODO: Implement GET endpoint to retrieve a specific book by ID
# Path: "/books/{book_id}"
# Should return the book if found, or 404 error if not found


# TODO: Implement POST endpoint to create a new book
# Path: "/books"
# Should accept a Book model, add it to books_db, and return 201 status


# TODO: Implement PUT endpoint to update an existing book
# Path: "/books/{book_id}"
# Should update the book if found, or return 404 error if not found


# TODO: Implement DELETE endpoint to remove a book
# Path: "/books/{book_id}"
# Should delete the book if found and return 204, or 404 if not found


# TODO: Implement GET endpoint to search books by author
# Path: "/books/search" with query parameter "author"
# Should return all books by the specified author


# Bonus: Add error handling for edge cases
# - Duplicate book IDs
# - Invalid data types
# - Empty strings for required fields
