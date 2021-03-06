#coding=utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'asdaflkr9y31hr9+_pugeap9oryhf3pw'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = 'hackgame'
    FLASKY_MAIL_SENDER = 'admin'
    FLASKY_ADMIN = os.environ.get('FLASK_ADMIN')
    FLASKY_POSTS_PER_PAGE = 20
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'prod.db')


    @staticmethod
    def init_app(app):

        pass


class DevelopmentConfig(Config):
    DEBUG = True



class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}