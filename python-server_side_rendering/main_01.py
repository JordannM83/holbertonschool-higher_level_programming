#!/usr/bin/python3
"""
Main file for testing task_01_jinja.py
Run the Flask application and test the routes:
- http://localhost:5000/
- http://localhost:5000/about
- http://localhost:5000/contact
"""
from task_01_jinja import app

if __name__ == '__main__':
    app.run(debug=True, port=5000)
