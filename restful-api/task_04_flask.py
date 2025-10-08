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
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Data endpoint - returns list of usernames"""
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """Status endpoint"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Get user by username"""
    try:
        return jsonify(users[username])
    except KeyError:
        return jsonify({"error": "User not found"})


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user"""
    data = request.get_json()
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    users[data["username"]] = data
    return jsonify({
                    "message": "User added",
                    "user": data
                    }), 201


if __name__ == '__main__':
    app.run()
