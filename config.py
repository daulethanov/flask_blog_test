class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost:5432/flask_blog"
    SECRET_KEY = 'sgdsfsdagfvfgrhgfdvsgrg'
    SECURITY_REGISTERABLE = True
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'