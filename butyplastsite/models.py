from app import db
from datetime import datetime
import re

def slugify(title):
    pattern = r'[^\w+]'
    return re.sub(pattern, '_', title)

def slugify_date(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '', s)

class Articles(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(150), unique=True)
    created = db.Column(db.DateTime, default=datetime.now())
    title = db.Column(db.String(150))
    body = db.Column(db.Text)
    specification = db.Column(db.Text)
    image = db.Column(db.String(150))

    def __init__(self, *args, **kwargs):
        super(Articles, self).__init__(*args, **kwargs)
        self.slug = slugify(self.title) + '_' + slugify_date(str(datetime.now()))

    def __repr__(self):
        return '<Article %r, id: %r>' % (self.title, self.id)




# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     page = db.Column(db.String(20))
#     image = db.Column(db.String(100))
#     heading = db.Column(db.String(100))
#     text = db.Column(db.String(500))
#     price = db.Column(db.Float)
#     link = db.Column(db.String(100))


