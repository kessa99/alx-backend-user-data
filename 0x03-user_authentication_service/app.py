#!/usr/bin/env python3
"""
Route module for the API
"""
import logging
from flask import Flask, jsonify, request, abort
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

    @app.route('/sessions', methods=['POST'], strict_slashes=False)
    def login() -> str:
        """POST /sessions
        Return:
          - 401: if email or password is incorrect
          - 200: if login is successful
        """
        email, password = request.form.get('email'), request.form.get('password')
        if not AUTH.valid_login(email, password):
            abort(401)
        session_id = AUTH.create_session(email)
        result = jsonify({"email": email, "message": "logged in"}), 200
        result.status_code = 200
        result.set_cookie("session_id", session_id)
        return result

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")