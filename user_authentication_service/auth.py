#!/usr/bin/env python3
"""Hash password"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Method that takes in a password string arguments and returns bytes"""
    salt = bcrypt.gensalt()
    _hash_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return _hash_password
