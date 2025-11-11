#!/usr/bin/python3
"""
Main file for testing task_03_files.py
Run the Flask application and test the routes:
- http://localhost:5000/products?source=json
- http://localhost:5000/products?source=csv
- http://localhost:5000/products?source=json&id=1
- http://localhost:5000/products?source=csv&id=2
- http://localhost:5000/products?source=xml (invalid source)
"""
from task_03_files import app

if __name__ == '__main__':
    app.run(debug=True, port=5000)
