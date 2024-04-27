#!/usr/bin/env python3
"""
Main file
"""
from users.auth import Auth
auth = Auth()
print(auth._hash_password("Hello Holberton"))