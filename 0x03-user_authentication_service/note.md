***Mon code***
```javascript
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
```

***correction***
```javascript
    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user
        """
        try:
            user = self.find_user_by(id=user_id)
        except NoResultFound:
            raise NoResultFound("No result found")
            
            
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError("User haf no attribute {}".format(key))
            setattr(user, key, value)
        
        try:
            self._session.commit()
        except InvalidRequestError:
            raise
```