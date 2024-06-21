#!/usr/bin/env python3
"""
Auth class for API authentication management
"""
from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summary_

        Args:
            path (str): _description_
            excluded_paths (List[str]): _description_

        Returns:
            bool: _description_
        """
        return True

    def authorization_header(self, request=None) -> str:
        """
        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """_summary_

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            User: _description_
        """
        return None
