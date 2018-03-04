class Configuretion(object):
    
    DEBUG = True # del_string

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1987@localhost/butyplast'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'hard to guess string'
# del_string
    UPLOAD_FOLDER = '/home/stariy/andrey/butyplast/site/butyplastsite/static/uploads'