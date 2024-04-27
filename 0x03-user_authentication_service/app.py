#!/usr/bin/env python3
"""
Route module for the API
"""
import logging
from flask import Flask, jsonify, request
from auth import Auth
# logging.disable(logging.WARNING)

AUTH = Auth()

app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    WELCOME
    """
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """
    create user
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        # find_user = auth.find_user_by(email)
        # if find_user:
        #     return jsonify({"message": "User {} already exists".format(email)}), 400

        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")