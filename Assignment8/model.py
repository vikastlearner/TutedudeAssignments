# Flask-SQLAlchemy for DB
from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy instance
db = SQLAlchemy()

# SQLAlchemy Tables:
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String, unique=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    city = db.Column(db.String(100))
    password = db.Column(db.String(100), nullable=False)