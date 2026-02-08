# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will learn how to build a modern REST API using the FastAPI framework. You'll create a book management API that handles CRUD operations (Create, Read, Update, Delete) and includes data validation, proper HTTP status codes, and interactive API documentation.

## 📝 Tasks

### 🛠️	Task 1: Set Up FastAPI and Create Basic Endpoints

#### Description
Install FastAPI and create your first API with basic GET endpoints. You'll set up the development environment, create a FastAPI application instance, and implement endpoints to retrieve book information.

#### Requirements
Completed program should:

- Install FastAPI and uvicorn (ASGI server) using pip
- Create a FastAPI application instance
- Implement a GET endpoint at `/` that returns a welcome message
- Implement a GET endpoint at `/books` that returns a list of all books
- Implement a GET endpoint at `/books/{book_id}` that returns a specific book by ID
- Run the application using uvicorn and verify endpoints work


### 🛠️	Task 2: Implement POST and PUT Endpoints with Data Validation

#### Description
Add functionality to create new books and update existing ones. Use Pydantic models to validate incoming data and ensure proper data structure.

#### Requirements
Completed program should:

- Create a Pydantic model called `Book` with fields: id, title, author, year, and genre
- Implement a POST endpoint at `/books` to add a new book to the collection
- Implement a PUT endpoint at `/books/{book_id}` to update an existing book
- Validate that required fields are present and have correct data types
- Return appropriate HTTP status codes (201 for creation, 200 for updates, 404 if book not found)
- Handle duplicate IDs appropriately


### 🛠️	Task 3: Add DELETE Endpoint and Explore API Documentation

#### Description
Complete the CRUD operations by implementing a DELETE endpoint. Then explore FastAPI's automatic interactive API documentation to test all your endpoints.

#### Requirements
Completed program should:

- Implement a DELETE endpoint at `/books/{book_id}` to remove a book from the collection
- Return 204 No Content on successful deletion or 404 if book not found
- Test all endpoints using FastAPI's interactive documentation at `/docs` (Swagger UI)
- Verify that the API correctly handles edge cases (invalid IDs, missing books, invalid data)
- Add a GET endpoint at `/books/search?author={author_name}` to filter books by author


