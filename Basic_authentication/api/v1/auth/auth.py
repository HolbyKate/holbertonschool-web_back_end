#!/usr/bin/env python3
""" Module of auth
"""
from flask import request
from typing import List, TypeVar


"""Define generic User type"""
User = TypeVar('User')


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summary_

        Args:
            path (str): _description_
            excluded_paths (List[str]): _description_

        Returns:
            bool: _description_
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        return None

    def current_user(self, request=None) -> User:
        """_summary_

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            User: _description_
        """
        return None
