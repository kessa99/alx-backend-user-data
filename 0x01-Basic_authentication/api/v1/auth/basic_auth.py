#!/usr/bin/env python3
"""
basic auth class
"""
from flask import jsonify, abort, request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class to manage the API authentication"""
    pass
