import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'use xkcd password generator'
    SQLALCHEMY_DATABASE_URI = 'sqlite:/// path to db'