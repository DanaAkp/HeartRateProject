import logging
import traceback

from flask_login import logout_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager
from app.models import User


@login_manager.user_loader
def load_user(user_id: int) -> User:
    return User.query.filter(User.id == int(user_id)).one_or_none()


class UserService:
    AUTH_ERROR = 'Invalid data for login.'

    @classmethod
    def create_user(cls, email: str, password: str, name: str, surname: str) -> dict:
        try:
            user = User()
            user.email = email
            user.hash_password = generate_password_hash(password)
            user.name = name
            user.surname = surname

            db.session.add(user)
            db.session.commit()
            return user.view()
        except Exception as error:
            db.session.rollback()
            logging.error(f'Error: {error}, traceback: {traceback.format_exc()}')
            raise Exception('Failed to create user.')

    @classmethod
    def login(cls, email: str, password: str) -> dict:
        if not (user := User.query.filter(User.email == email).one_or_none()) \
                and not check_password_hash(user.hash_password, password):
            raise ValueError(cls.AUTH_ERROR)
        login_user(user, remember=True)
        return user.view()

    @classmethod
    def logout(cls) -> dict:
        logout_user()
        return {'success': True}
