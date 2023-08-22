import flask_login
from flask import request
from flask_restx import Resource

from app import user_api
from app.controllers.user_service import UserService
from app.views.swagger_models import request_user_data, response_user_data, login_data


@user_api.route('/', methods=['POST'])
class CreateUsers(Resource):
    @user_api.expect(request_user_data, validate=True)
    @user_api.response(200, 'Success', response_user_data)
    def post(self):
        """Create new user."""
        data = request.get_json()
        result = UserService.create_user(
            email=data.get('email'),
            password=data.get('password'),
            name=data.get('name'),
            surname=data.get('surname'),
        )
        return result


@user_api.route('/login', methods=['POST'])
class LoginUsers(Resource):
    @user_api.expect(login_data, validate=True)
    @user_api.response(200, 'Success', response_user_data)
    def post(self):
        """Login user by email and password."""
        data = request.get_json()
        result = UserService.login(
            email=data.get('email'),
            password=data.get('password')
        )
        return result


@user_api.route('/logout', methods=['POST'])
class LogoutUsers(Resource):
    @user_api.response(200, 'Success')
    @flask_login.login_required
    def post(self):
        """Logout user."""
        return UserService.logout()
