#!/usr/bin/env python3
"""
Auth class for API authentication management
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """Session Auth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session ID for user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Method that returne a User Id based on a session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Instance method that returns User instance based on cookie value"""
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        try:
            user = User.get(user_id)
        except Exception:
            return None

        return user
