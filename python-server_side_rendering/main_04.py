#!/usr/bin/python3
"""
Main file for testing task_04_db.py
First, create the database, then run the Flask application
Test the routes:
- http://localhost:5000/products?source=json
- http://localhost:5000/products?source=csv
- http://localhost:5000/products?source=sql
- http://localhost:5000/products?source=sql&id=1
"""
import sqlite3

def create_database():
    """Create and populate the products.db database"""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Use INSERT OR IGNORE to avoid duplicates
    cursor.execute('''
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    conn.commit()
    conn.close()
    print("Database ready!")

if __name__ == '__main__':
    # Create the database first
    create_database()
    
    # Run the Flask application
    from task_04_db import app
    app.run(debug=True, port=5000)
