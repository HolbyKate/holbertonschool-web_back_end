#!/usr/bin/env python3
"""
Auth class for API authentication management
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """ Auth class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summary_

        Args:
            path (str): _description_
            excluded_paths (List[str]): _description_

        Returns:
            bool: _description_
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        """assume excluded_paths contains string path always ending by a /"""
        if not path.endswith('/'):
            path += '/'
        """Check if the path is in the excluded_paths"""
        for excluded_path in excluded_paths:
            if excluded_path.endswith('/') and path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """_summary_

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            User: _description_
        """
        return None

    def session_cookie(self, request=None):
        """Method that returns a cookie value from a request"""
        if request is None:
            return None
        session_name = os.getenv("SESSION_NAME", "my_session_id")
        return request.cookie.get(session_name)
