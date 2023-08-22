from flask_login import UserMixin

from app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.INTEGER, primary_key=True)
    email = db.Column(db.VARCHAR(50), unique=True, nullable=False)
    hash_password = db.Column(db.String, unique=True, nullable=False)

    name = db.Column(db.VARCHAR(100), nullable=False)
    surname = db.Column(db.VARCHAR(100), nullable=False)

    average_heart_rate = db.Column(db.Integer)
    heart_rates = db.relationship('HeartRate')

    def view(self) -> dict:
        return dict(
            id=self.id,
            email=self.email,
            name=self.name,
            surname=self.surname,
            average_heart_rate=self.average_heart_rate
        )
