#!/usr/bin/python3
"""
Main file for testing task_02_logic.py
Run the Flask application and test the route:
- http://localhost:5000/items
"""
from task_02_logic import app

if __name__ == '__main__':
    app.run(debug=True, port=5000)
