import os


class Config:
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = f'postgresql://postgres:{os.environ["PG_PASS"]}@localhost:5432/tasklerdb'
