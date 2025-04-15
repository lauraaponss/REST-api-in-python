#!/usr/bin/env python3
"""
Library REST API
Design of Telematic Systems, UC3M

This program implements a RESTful API for a library system using Flask.
Authors:
	Lucas Kohley Aguilar - 100497018
	Laura Pons García - 100496761
"""

from flask import Flask, jsonify
from utilsAPI import read_books_from_csv

app = Flask(__name__)

# Global variable to store books
books = {}

def load_books():
    """Load books from CSV file into global dictionary"""
    global books
    books_list = read_books_from_csv()
    books = {book['id']: book for book in books_list}

@app.route('/api/books', methods=['GET'])
def get_books():
    """Get all books"""
    return jsonify(list(books.values())), 200

@app.route('/api/books/<book_id>', methods=['GET'])
def get_books_by_id(book_id):
    """Get a specific book by ID"""
    book = books.get(book_id)
    if book:
        return jsonify(book), 200
    return jsonify({'error': 'Book not found'}), 404

@app.route('/api/books/search/<title>', methods=['GET'])
def search_books_by_title(title):
    """Search books by title"""
    matching_books = [
        book for book in books.values()
        if title.lower() in book['title'].lower()
    ]
    
    if matching_books:
        return jsonify(matching_books), 200
    return jsonify({'error': 'No books found with that title'}), 404

@app.route('/api/books/<book_id>', methods=['DELETE'])
def delete_book_by_id(book_id):
    """Delete a book by ID"""
    if book_id in books:
        del books[book_id]
        return jsonify({}), 200
    return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    # Load books when server starts
    load_books()
    print("Server started! Books loaded from CSV.")
    app.run(debug=True)
