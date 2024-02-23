#!/usr/bin/env python3

"""Auth module"""

from sqlalchemy.orm.exc import NoResultFound
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hash a password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

        raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login credentials."""
        try:
            user = self._db.find_user_by(email=email)
            return (
                bcrypt.checkpw(password.encode(),
                               user.hashed_password.encode())
            )
        except NoResultFound:
            return False
