#!/usr/bin/env python3
"""
View for Session Authentication
"""
from flask import request, jsonify, abort, make_response
from api.v1.app import auth
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Handles user login and creates a session"""

    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        found_users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not found_users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in found_users:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    response = make_response(jsonify(user.to_json()))
    session_name = getenv('SESSION_NAME')
    response.set_cookie(session_name, session_id)

    return response
