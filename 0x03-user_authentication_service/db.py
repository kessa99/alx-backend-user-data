#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
    
    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a user to the database
        """
        user = User(email=email, hashed_password=hashed_password)
        try:
            self._session.add(user)
            self._session.commit()
        except Exception as e:
            print(f'Error: {e}')
            self._session.rollback()
            raise
        return user
    
    def find_user_by(self, **kwargs) -> User:
        """Find a user by a specific attribute
        """
        try:
            find = self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("No result found")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid request")
        return find
    
    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user
        """
        user = self.find_user_by(id=user_id)
        try:
            if user is None:
                raise NoResultFound
            else:
                for key, value in kwargs.items():
                    setattr(user, key, value)

                self._session.commit()
        except InvalidRequestError:
            raise
