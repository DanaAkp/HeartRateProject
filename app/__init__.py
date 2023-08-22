import os
from dotenv import load_dotenv
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

load_dotenv()
app = Flask(__name__)

app.config.from_object('config.%s' % (os.environ.get("FLASK_ENV")))

bootstrap = Bootstrap(app)

db = SQLAlchemy(app)
print(f"Start APP, DB connect: {app.config.get('SQLALCHEMY_DATABASE_URI')}")


login_manager = LoginManager(app)


api = Api(
    app,
    version='1.0',
    title='My Swagger',
    description='Swagger Rest API',
    doc='/my-swagger/',
)

user_api = api.namespace('api/users', description='User endpoints')
heart_rate_api = api.namespace('api/heart_rates', description='Heart rate endpoints')

from app.models import *  # noqa
from app.views import *  # noqa

with app.app_context():
    db.create_all()
