#!/usr/bin/env python3
"""
Library API Test Script
Design of Telematic Systems, UC3M

This script tests the library API endpoints.
Authors:
	Lucas Kohley Aguilar - 100497018
	Laura Pons García - 100496761
"""

import requests
import json

def test_api():
    """Test all API endpoints"""
    BASE_URL = 'http://localhost:5000/api'
    
    def print_response(response, test_name):
        """Helper function to print response details"""
        print(f"\n=== {test_name} ===")
        print(f"Status Code: {response.status_code}")
        print("Response:")
        print(json.dumps(response.json(), indent=2))
        print("=" * 50)

    # Test 1: Get all books
    response = requests.get(f"{BASE_URL}/books")
    print_response(response, "Getting all books")

    # Test 2: Get book #2 (To Kill a Mockingbird)
    response = requests.get(f"{BASE_URL}/books/2")
    print_response(response, "Getting book #2")

    # Test 3: Delete book #2
    response = requests.delete(f"{BASE_URL}/books/2")
    print_response(response, "Deleting book #2")

    # Test 4: Try to get deleted book #2 (should fail)
    response = requests.get(f"{BASE_URL}/books/2")
    print_response(response, "Trying to get deleted book #2")

    # Test 5: Get book #5 (The Catcher in the Rye)
    response = requests.get(f"{BASE_URL}/books/5")
    print_response(response, "Getting book #5")

    # Test 6: Delete book #5
    response = requests.delete(f"{BASE_URL}/books/5")
    print_response(response, "Deleting book #5")

    # Additional test: Search for a book by title
    response = requests.get(f"{BASE_URL}/books/search/lord")
    print_response(response, "Searching for 'lord' in titles")

if __name__ == "__main__":
    test_api()
