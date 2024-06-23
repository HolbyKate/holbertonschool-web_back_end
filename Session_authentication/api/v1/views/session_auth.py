#!/usr/bin/env python3
"""View for Session Authentication"""

from flask import Blueprint, request, jsonify
from models.user import User
import os

session_auth = Blueprint('session_auth', __name__)


@session_auth.route(
    '/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    from api.v1.app import auth  # Import here to avoid circular import issues

    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    user_json = user.to_json()

    response = jsonify(user_json)
    cookie_name = os.getenv('SESSION_NAME')
    response.set_cookie(cookie_name, session_id)

    return response
