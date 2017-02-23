from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from markdown import markdown
import bleach
from flask import current_app, request
from flask_login import UserMixin, AnonymousUserMixin
from .. import db, login_manager

class Messages(db.Model):
    __tablename__='messages'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(40))
    content=db.Column(db.Text)
    token=db.Column(db.String(40))

    @staticmethod
    def fetch_messages_by_token(token):
        return Messages.query.filter_by(token=token).all()

    @staticmethod
    def fetch_message_by_id(id):
        message=Messages.query.filter_by(id=id).first()
        return message
    @staticmethod
    def add_message(name,content,token):
        message=Messages()
        message.token=token
        message.name=name
        message.content=content
        print content
        print token
        db.session.add(message)
        db.session.commit()

    @staticmethod
    def delete_message(id):
        message=Messages.fetch_message_by_id(id)
        db.session.delete(message)
        db.session.commit()


