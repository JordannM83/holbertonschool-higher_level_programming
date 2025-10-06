#!/usr/bin/python3
"""
Simple Flask API
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Users dictionary (do not include test data)
users = {}


@app.route('/')
def home():
    """Home endpoint"""
    pass


@app.route('/data')
def get_data():
    """Data endpoint - returns list of usernames"""
    pass


@app.route('/status')
def get_status():
    """Status endpoint"""
    pass


@app.route('/users/<username>')
def get_user(username):
    """Get user by username"""
    pass


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user"""
    pass


if __name__ == '__main__':
    app.run()
