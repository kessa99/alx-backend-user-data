#!/usr/bin/env python3
"""Users models."""
from uuid import uuid4
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    id: str
    email: str
    hashed_password: str
    session_id: str
    reset_token: str
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    # def __init__(self, email, hashed_password):
    #     self.id = str(uuid4())
    #     self.email = email
    #     self.hashed_password = hashed_password
    #     self.session_id = None
    #     self.session_token = None
    #     self.reset_token = None