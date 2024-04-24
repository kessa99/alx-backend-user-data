#!/usr/bin/activate
"""
Main file
"""
import bcrypt
from users.user import User
from users.db import DB
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from flask import jsonify

class Auth:
    """
    Auth class
    """
    def __init__(self):
        """
        Constructor
        """
        self._db = DB()

    def _hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed

    def register_user(self, email: str, password: str) -> User:
        """
        Register user
        """
        try:
            existing_email = self._db.find_user_by(email=email)
            #verifier si l'email exist
            if existing_email:
                return jsonify({"message": "User {} already exists".format(email)}), 400

            # hasher le mot de passe si l'email n'existe pas
            hashed_password = self.hash_password(password)

            #enregistrer le nouvel user a la base de donne
            user = self._db.add_user(email, hashed_password)

            return user
        except NoResultFound:
            return jsonify({"message": "User {} already exists".format(email)}), 400

        except ValueError:
            return None



    # def is_valid(self, hashed_password: str, password: str) -> bool:
    #     """
    #     Validate password
    #     """
    #     return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

