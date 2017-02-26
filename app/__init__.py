from flask import Flask,session,render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_pagedown import PageDown
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from flask_cors import CORS, cross_origin
import os
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)


    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)

    # from api.Users import user as user_blueprint
    # from api.Courses import course as course_blueprint
    # app.register_blueprint(user_blueprint, url_prefix='/api/users')
    # app.register_blueprint(course_blueprint, url_prefix='/api/courses')
    # from . import micourse as micourse_blueprint
    # app.register_blueprint(micourse_blueprint, url_prefix='/')
    # from micourse import micourse as micourse_blueprint
    # from api import api as api_blueprint
    from hackgame1 import hackgame1 as hackgame1_blueprint
    # app.register_blueprint(api_blueprint, url_prefix='/api')
    # app.register_blueprint(micourse_blueprint)
    @app.route('/')
    def index():
        return redirect(url_for('hackgame1.index'))
    app.register_blueprint(hackgame1_blueprint,url_prefix="/hackgame1")
    app.permanent_session_lifetime = timedelta(minutes=5)

    return app