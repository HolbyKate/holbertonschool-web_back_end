#!/usr/bin/env python3
"""
Auth class for API authentication management
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Session Auth class"""
    pass
