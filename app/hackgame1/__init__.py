from flask import Blueprint

hackgame1=Blueprint("hackgame1",__name__)

from datetime import timedelta
from flask import session, app

from ..utils.random_token import  random_token
@hackgame1.before_request
def make_session_permanent():
    if session.get('token') is None:
        session['token'] = random_token()
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=60*24)
from . import views
