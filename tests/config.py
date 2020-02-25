from pathlib import Path

ENV = 'development'
TESTING = True
SQLALCHEMY_DATABASE_URI = f'sqlite:///{Path.cwd().resolve()}/dev.db'
SECRET_KEY = 'test-environment'
SQLALCHEMY_TRACK_MODIFICATIONS = False
