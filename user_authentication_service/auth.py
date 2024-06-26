#!/usr/bin/env python3
"""Hash password"""

import bcrypt

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Method that takes in a password string arguments and returns bytes"""
    salt = bcrypt.gensalt()
    _hash_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return _hash_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """initialization"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registrer user"""
        try:
            """Try to find the user by email"""
            self._db.find_user_by(email=email)
            """if email already existe"""
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            """if no email found, we do the registration"""
        hashed_password = self._hash_password(password)
        return self._db.add_user(email, hashed_password)
