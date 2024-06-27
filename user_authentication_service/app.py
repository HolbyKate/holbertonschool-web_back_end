#!/usr/bin/env python3
"""Set up Flask"""

from flask import Flask, jsonify, request

from auth import Auth


app = Flask(__name__)

AUTH = Auth()


@app.route('/', methods=['GET'])
def welcome():
    """GET json data"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register_user():
    """Register user"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/session', methods=['POST'])
def login():
    """Create login"""
    email = request.form.get("email")
    password = request.form.get("password")
    
    try:
        AUTH.valid_login(email, password)
    except ValueError:
        return jsonify({"email": "<user email>", "message": "logged in"})
    else:
        abort(401)  
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
