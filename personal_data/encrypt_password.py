#!/usr/bin/env python3
"""Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """function that expects one string argument name password and
    returns a salted, hashed password, which is a byte string."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """implement is_valid function"""
    if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
        return True
    return False
