#!/usr/bin/env python3
"""Hash password"""

import bcrypt

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """initialization"""
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """
        Method that takes in a password string arguments and returns bytes
        """
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

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
            """Add user to the database and return the User object"""
            user = self._db.add_user(
                email=email, hashed_password=hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Method taht expect email and password required arguments
        and return a boolean
        """
        try:
            user = self._db.find_user_by(email=email)
            if user and bcrypt.checkpw(password.encode('utf-8'),
                                      user.hashed_password):
                return True
        except NoResultFound:
            pass
        return False
