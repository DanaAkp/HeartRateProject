import logging
import traceback

from sqlalchemy import func

from app import db
from app.models import HeartRate, User


class HeartRateService:
    @classmethod
    def get_average_heart_rate(cls, user_id: int) -> float:
        average_query = db.session.query(
            func.avg(HeartRate.heart_rate).label('avg'),
        ).filter(HeartRate.user_id == user_id) \
            .group_by(HeartRate.user_id).first()

        average = average_query.avg
        return average

    @classmethod
    def add_heart_rate_record(cls, heart_rate: int, user_id: int) -> HeartRate:
        if not (user := User.query.filter(User.id == user_id).one_or_none()):
            raise Exception(f'Not found user by id {user_id}')

        try:
            heart_rate_record = HeartRate(
                user_id=user_id,
                heart_rate=heart_rate
            )
            db.session.add(heart_rate_record)
            db.session.flush()
            user.average_heart_rate = cls.get_average_heart_rate(user_id)
            db.session.flush()
        except Exception as error:
            db.session.rollback()
            logging.error(f'Error: {error}, traceback: {traceback.format_exc()}')
            raise Exception('Failed to create heart rate record.')

        db.session.commit()
        result = user.view()
        result.update({'current_heart_rate': heart_rate})
        return result

    @classmethod
    def get_last_record(cls, user_id: int) -> dict:
        last_record = HeartRate.query \
            .filter(HeartRate.user_id == user_id) \
            .order_by(HeartRate.create_time.desc()).first()
        return last_record.view()
