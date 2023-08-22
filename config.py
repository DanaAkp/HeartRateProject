import os


class Config(object):
    SECRET_KEY = ':N(4w4AV8L@6s$TA-9U4in/ZiL'

    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', '5432')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'test')
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}" \
                              f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


class DevelopmentConfig(Config):
    DEBUG = True
