from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    face_image = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username