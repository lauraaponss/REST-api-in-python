# Library REST API

A RESTful API for managing a library system, developed using Flask. This project was created as part of the Design of Telematic Systems course at UC3M.

## 📚 Overview

This application provides a simple yet functional RESTful API for library management. It allows users to retrieve book information, search for books by title, and delete books from the library database.

The project consists of three Python files:
- **library.py**: Main application file that defines the API endpoints and server
- **utilsAPI.py**: Utility functions for data processing
- **test_library.py**: Test script for verifying API functionality

## 🛠️ Features

- **RESTful Architecture**: Follows REST principles for API design
- **CRUD Operations**: Currently supports Read and Delete operations
- **Search Functionality**: Search for books by title
- **CSV Data Storage**: Books are loaded from a CSV file
- **Comprehensive Testing**: Includes a test script to validate all endpoints

## 🔄 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/books` | GET | Get all books in the library |
| `/api/books/<book_id>` | GET | Get a specific book by ID |
| `/api/books/search/<title>` | GET | Search books by title (partial match) |
| `/api/books/<book_id>` | DELETE | Remove a book from the library |

## 📦 Requirements

- Python 3.x
- Flask
- Requests (for testing)

## 📋 Installation

1. Clone this repository
2. Install required packages:
   ```bash
   pip install flask requests
   ```
3. Ensure you have a properly formatted CSV file named `books.csv` in the same directory

## 🚀 How to Run

### Starting the Server

```bash
python library.py
```

The Flask server will start on http://localhost:5000

### Running the Tests

```bash
python test_library.py
```

This will execute a series of tests against the running server and display the results.

## 📝 CSV File Format

The API expects a CSV file with the following structure:

```
id,title,author,year,genre
1,To Kill a Mockingbird,Harper Lee,1960,Fiction
2,1984,George Orwell,1949,Dystopian
...
```

## 📋 Example Response

Getting all books (`GET /api/books`):

```json
[
  {
    "id": "1",
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year": "1960",
    "genre": "Fiction"
  },
  {
    "id": "2",
    "title": "1984",
    "author": "George Orwell",
    "year": "1949",
    "genre": "Dystopian"
  },
  ...
]
```

## 🔍 Future Improvements

- Add POST endpoint to add new books
- Add PUT endpoint to update existing books
- Implement database storage instead of CSV
- Add authentication for secure operations
- Add pagination for large datasets

## 👥 Author

- Laura Pons García - 100496761

## 📚 Course Information

Developed for the Design of Telematic Systems course at Universidad Carlos III de Madrid (UC3M).

