#!/usr/bin/env python3
"""Hash password"""

import bcrypt
import hashlib
import os


def _hash_password(password: str) -> bytes:
    """Method that takes in a password string arguments and returns bytes"""

    salt = os.urandom(32)
    _hashed_password = hashlib.pbkdf2_hmac(
        'sha256', password.encode('utf-8'), salt, 100000
        )
    return salt + _hashed_password
