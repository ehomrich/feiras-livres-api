from pathlib import Path

from decouple import config

BASE_DIR = Path.cwd().resolve()


class AppConfig:
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default=f'sqlite:///{BASE_DIR}/dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = config('SQLALCHEMY_ECHO', cast=bool, default=False)
