#!/usr/bin/env python3
"""
Main file
"""
import logging
import bcrypt
from user import User
from db import DB
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from flask import jsonify
from uuid import uuid4

logging.disable(logging.WARNING)

def _hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def _generate_uuid() -> str:
    """
    Generate a UUID
    """
    return str(uuid4())

class Auth:
    """
    Auth class
    """
    def __init__(self):
        """
        Constructor
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            pass
            # print(existing_email)
            #verifier si l'email exist
            # if existing_email:
            #     raise ValueError("User {} already exists".format(email))

            # hasher le mot de passe si l'email n'existe pas
            hashed_password = _hash_password(password)

            #enregistrer le nouvel user a la base de donne
            user = self._db.add_user(email, hashed_password)

            return user
        # except NoResultFound as e:
        #     return {"message": str(e)}, 400

        # except ValueError:
        #     return None
    
    def find_user_by(self, **kwargs) -> User:
        """
        Find user by a specific attribute
        """
        try:
            user = self._db.find_user_by(**kwargs)
            return user
        except InvalidRequestError:
            return None

    def valid_login(self, email:str, password: str) -> bool:
        """
        validation login
        """
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                password = password.encode('utf-8')
                hased_password = user.hashed_password
                if bcrypt.checkpw(password, user.hashed_password):
                    return True
        
        except NoResultFound:
            return False
        return False
        
    
    def create_session(self, email: str) -> str:
        """
        Create a new session
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
                return session_id
            return {"message": "User {} does not exist".format(email)}, 400
        except NoResultFound:
            return None

    # def is_valid(self, hashed_password: str, password: str) -> bool:
    #     """
    #     Validate password
    #     """
    #     return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

