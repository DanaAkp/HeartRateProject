import re

from flask_restx import fields, reqparse
from app import user_api


class EmailField(fields.String):
    REG_EMAIL = r'([^@\s]{2,}@[^@\\.\s]{2,}\.[^@\s]{2,}$)'

    def parse(self, value: str) -> str:
        if re.search(self.REG_EMAIL, value):
            return value
        raise ValueError('Invalid email format.')


request_user_data = user_api.model(
    'RequestUserData',
    {
        'name': fields.String(required=True),
        'surname': fields.String(required=True),
        'email': EmailField(required=True),
        'password': fields.String(required=True),
    }
)

response_user_data = user_api.model(
    'ResponseUserData',
    {
        'id': fields.Integer(required=True),
        'name': fields.String(required=True),
        'surname': fields.String(required=True),
        'email': EmailField(required=True),
        'password': fields.String(required=True),
        'average_heart_rate': fields.Float()
    }
)


request_heart_rate_data = user_api.model(
    'RequestHeartRateData',
    {
        'current_heart_rate': fields.Integer(required=True)
    }
)

response_heart_rate_data = user_api.model(
    'ResponseHeartRateData',
    {
        'heart_rate': fields.Integer(required=True),
        'create_time': fields.DateTime(required=True)
    }
)

response_add_heart_rate_data = user_api.model(
    'ResponseAddHeartRateData',
    {
        'user_id': fields.Integer(required=True),
        'name': fields.String(required=True),
        'surname': fields.String(required=True),
        'email': EmailField(required=True),
        'password': fields.String(required=True),
        'average_heart_rate': fields.Float(),
        'current_heart_rate': fields.Integer()
    }
)

login_data = user_api.model('LoginData', {
    'email': EmailField(required=True),
    'password': EmailField(required=True),
})
