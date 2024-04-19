#!/usr/bin/env python3
"""
auth class
"""
from flask import jsonify, abort, request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Public method to require authentication"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Public method to authorize the header"""
        key = 'Authorization'
        if request is None or key not in request.headers:
            return None
        return request.headers.get(key)

    def current_user(self, request=None) -> TypeVar('User'):
        """Public method to return the current user"""
        return None
