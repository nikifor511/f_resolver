from __init__ import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    additional = db.Column(db.Text)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    type = db.Column(db.Integer)
    isLogin = db.Column(db.Boolean)

    def __init__(self, username, additional, email, password_hash, type, isLogin):
        self.username = username
        self.additional = additional
        self.email = email
        self.password_hash = password_hash
        self.type = type
        self.isLogin = isLogin

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dt_begin = db.Column(db.DateTime,  index=True, default=datetime.utcnow)
    dt_end = db.Column(db.DateTime)
    title = db.Column(db.Text)
    describe = db.Column(db.Text)
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    images = db.Column(db.Text)
    chat = db.Column(db.Text)


    def __repr__(self):
        return '<Post {}>'.format(self.body)

