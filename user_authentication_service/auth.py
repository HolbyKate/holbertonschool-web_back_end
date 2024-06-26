#!/usr/bin/env python3
"""Hash password"""

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Initialization"""
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """
        Method that takes in a password string argument and returns bytes.
        The returned bytes is a salted hash of the input password,
        hashed with bcrypt.hashpw.
        """
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def _generate_uuid(self) -> str:
        """Generate a unique UUID string."""
        return str(uuid.uuid4())

    def register_user(self, email: str, password: str) -> User:
        """Register user."""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            user = self._db.add_user(
                email=email, hashed_password=hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Method that expects email and password arguments and returns a boolean.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False
