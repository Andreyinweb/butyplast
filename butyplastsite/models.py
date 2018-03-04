from app import db
from datetime import datetime
import re


class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    page = db.Column(db.String(20))
    image = db.Column(db.String(100))
    heading = db.Column(db.String(100))
    text = db.Column(db.String(500))
    price = db.Column(db.Float)
    link = db.Column(db.String(100))
db.create_all()