import os
import sys


basedir = os.path.abspath(os.path.dirname(__file__))

if os.path.exists('../config.env'):
    print('Importing environment from .env file')
    for line in open('../config.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1].replace("\"", "")


class Configuretion(object):
    # В файл config.env записывать без пробелов
    DEBUG = os.environ.get('DEBUG')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # del_string
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
