import flask_login
from flask import request
from flask_login import current_user
from flask_restx import Resource

from app import heart_rate_api
from app.controllers.heart_rate_service import HeartRateService
from app.views.swagger_models import response_add_heart_rate_data, request_heart_rate_data, response_heart_rate_data


@heart_rate_api.route('/heart_rates', methods=['POST', 'GET'])
class UserRequests(Resource):
    @heart_rate_api.expect(request_heart_rate_data, validate=True)
    @heart_rate_api.response(200, 'Success', response_add_heart_rate_data)
    @flask_login.login_required
    def post(self):
        """Add new heart rate record by user id."""
        data = request.get_json()
        result = HeartRateService.add_heart_rate_record(
            heart_rate=data.get('current_heart_rate'),
            user_id=current_user.id
        )
        return result

    @heart_rate_api.response(200, 'Success', response_heart_rate_data)
    @flask_login.login_required
    def get(self):
        """Get last heart rate record."""
        result = HeartRateService.get_last_record(
            user_id=current_user.id
        )
        return result
