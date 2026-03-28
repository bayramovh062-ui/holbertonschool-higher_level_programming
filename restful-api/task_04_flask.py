#!/usr/bin/python3
"""
This module sets up a simple API using the Flask framework.
It includes endpoints to get data, check status, and add users.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """
    This function returns a welcome message to the user.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """
    This function returns a JSON list of all usernames stored.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status_message():
    """
    This function returns the status message 'OK'.
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Returns the full object of the provided username.
    If the user does not exist, returns a 404 error.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Handles POST requests to add a new user.
    Validates the JSON payload and returns appropriate status codes.
    """
    parsed_data = request.get_json()

    if parsed_data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = parsed_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = parsed_data

    return jsonify({
        "message": "User added",
        "user": parsed_data
    }), 201


if __name__ == "__main__":
    app.run()
