#!/usr/bin/env python3
"""Set up Flask"""

from flask import Flask, jsonify, request, abort, make_response, sessions

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
    """Create login function"""
    email = request.form.get("email")
    password = request.form.get("password")

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = make_response(jsonify(
                {"email": email, "message": "logged in"}))
        response.set_cookie("session_id", session_id)
        return response, 200
    else:
        abort(401)

@app.route('/sessions', methods=['DELETE'])
def logout():
    """Create logoutfunction"""
    session_id = request.cookies.get('session_id')
    
    if session_id is None:
        abort(403)
    
    """If session Id is in the DB"""
    if session_id in sessions:
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
