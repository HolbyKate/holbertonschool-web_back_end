#!/usr/bin/env python3
"""
BasicAuth class that inherits from auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Empty class
    """
    def extract_base64_authorization_header(
        self, authorization_header: str
            ) -> str:
        """
        Method that returns the Base64 part of the Authorization header
        for a Basic Authentication
        """
        if authorization_header is None or not str:
            return None
        if not authorization_header.startswhith("Basic "):
            return None
        return authorization_header
