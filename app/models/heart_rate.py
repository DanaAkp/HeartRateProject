from datetime import datetime

from app import db


class HeartRate(db.Model):
    ___tablename__ = 'heart_rates'
    id = db.Column(db.INTEGER, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    heart_rate = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    users = db.relationship('User', back_populates='heart_rates')

    def view(self):
        return {
            'heart_rate': self.heart_rate,
            'create_time': self.create_time.strftime("%m/%d/%Y, %H:%M:%S"),
        }
