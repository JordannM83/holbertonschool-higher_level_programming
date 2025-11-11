#!/usr/bin/python3
"""
Task 3: Displaying Data from JSON or CSV Files in Flask
"""
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file():
    """Read and return data from products.json"""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def read_csv_file():
    """Read and return data from products.csv"""
    try:
        products = []
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert price to float and id to int
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        return []


@app.route('/products')
def products():
    # Get query parameters
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html',
                               error="Wrong source",
                               products=[])

    # Read data based on source
    if source == 'json':
        products = read_json_file()
    else:  # source == 'csv'
        products = read_csv_file()

    # Filter by id if provided
    if product_id:
        try:
            product_id = int(product_id)
            # Find product with matching id
            filtered_products = [p for p in products if p['id'] == product_id]
            if not filtered_products:
                return render_template('product_display.html',
                                       error="Product not found",
                                       products=[])
            products = filtered_products
        except ValueError:
            return render_template('product_display.html',
                                   error="Invalid id format",
                                   products=[])

    return render_template('product_display.html',
                           products=products,
                           error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
