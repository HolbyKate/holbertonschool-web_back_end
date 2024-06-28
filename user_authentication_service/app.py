#!/usr/bin/env python3
"""Set up Flask"""

from flask import Flask, jsonify, request, abort, make_response, redirect

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


@app.route('/sessions', methods=['POST'])
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
    """Find user associate with session_id"""
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    """Destroy session associate with user"""
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'])
def profile():
    """Implement profile function by session"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None or user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """Reset password"""
    email = request.form.get('email')
    if not AUTH.user_exists(email):
        abort(403)
    """Generate token reset"""
    reset_token = AUTH.generate_password_reset_token(email)
    return jsonify({"email": email, "reset_token": reset_token}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
