from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    _id = db.Column(db.Integer, primarykey=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50))
    location = db.Column(db.String(50))
    time_added = db.Column(db.DateTime, default = datetime.now)