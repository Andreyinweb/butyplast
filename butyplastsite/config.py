import os
import sys


basedir = os.path.abspath(os.path.dirname(__file__))

if os.path.exists('../config.env'):
    print('Importing environment from .env file')
    for line in open('../config.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1].replace("\"", "")

dirname = os.path.abspath(os.path.dirname(__file__))

class Configuretion(object):
    # В файл config.env записывать без пробелов и кавычек
    # In the file config.env write without spaces and quotation marks

    DEBUG = os.environ.get('DEBUG')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOAD_FOLDER = dirname + os.environ.get('UPLOAD_FOLDER')

    ##### flask_security
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')
    SECURITY_PASSWORD_HASH = os.environ.get('SECURITY_PASSWORD_HASH')