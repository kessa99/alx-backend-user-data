#!/usr/bin/env python3
"""
basic auth class
"""
from flask import jsonify, abort, request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth class to manage the API authentication"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract_base64_authorization_header
        """
        if authorization_header is None or \
                type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
    
    def decode_base64_authorization_header(self,
                                           decode_base64_authorization_header: str) -> str:
        """decode_base64_authorization_header"""

        if decode_base64_authorization_header is None or \
                type(decode_base64_authorization_header) is not str:
            return None
        try:
            return base64.b64decode(decode_base64_authorization_header).decode('utf-8')
        except Exception:
            return None
