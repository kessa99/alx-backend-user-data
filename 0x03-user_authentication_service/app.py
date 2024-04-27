#!/usr/bin/env python3
"""
Route module for the API
"""
import logging
from flask import Flask, jsonify
from views import app
from auth import Auth
logging.disable(logging.WARNING)

auth = Auth()

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    WELCOME
    """
    return jsonify({"message": "Bienvenue"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")