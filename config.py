import os

class DevConfig():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'abcd'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "mysql://movies_app:Movies_app%40123@localhost/movies_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = 'redis://localhost:4444/0'
    DEBUG = True
    
class ProdConfig():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://movies_app:Movies_app@123@localhost/movies_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = 'redis://localhost:4444/0'
    DEBUG = False


