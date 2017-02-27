from .. import db
from datetime import datetime

class Visitor(db.Model):
    __tablename__='visitor'
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    time=db.Column(db.DateTime,default=datetime.utcnow())
    ip=db.Column(db.String(40))

    @staticmethod
    def add_a_visitor(ip):
        visitor=Visitor()
        visitor.ip=ip
        db.session.add(visitor)
        db.session.commit()

    @staticmethod
    def fetch_visitor_number():
        return len(Visitor.query.all())
