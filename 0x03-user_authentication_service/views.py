#!/usr/bin/env python3
"""
views module
"""
import logging
from flask import Flask, jsonify, request, abort
from auth import Auth

logging.disable(logging.WARNING)

AUTH = Auth()
app = Flask(__name__)

@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """
    Create a new user.
    """
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        existing_user = AUTH.find_user_by(email=email)
        if existing_user:
            return jsonify({"message": "User {} already exists".format(email)}), 400
        else:
            AUTH.register_user(email, password)
            return jsonify({"email": email, "message": "user created"}), 200
    except ValueError as e:
        abort(400, {"message": str(e)})