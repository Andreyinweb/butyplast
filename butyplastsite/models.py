from app import db
from datetime import datetime
import re
from flask_security import UserMixin, RoleMixin

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
    # Связь с тадлицей Maintable
    id_main = db.Column(db.Integer, db.ForeignKey('maintable.id'))

    def __init__(self, *args, **kwargs):
        super(Articles, self).__init__(*args, **kwargs)
        self.slug = slugify(self.title) + '_' + slugify_date(str(datetime.now()))

    def __repr__(self):
        return '<Article %r, id: %r>' % (self.title, self.id)

class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(150), unique=True)
    created = db.Column(db.DateTime, default=datetime.now())
    title = db.Column(db.String(150))
    body = db.Column(db.Text)
    specification = db.Column(db.Text)
    price = db.Column(db.Float)
    image = db.Column(db.String(150))
    # Связь с тадлицей Maintable
    id_main = db.Column(db.Integer, db.ForeignKey('maintable.id'))

    def __init__(self, *args, **kwargs):
        super(Products, self).__init__(*args, **kwargs)
        self.slug = slugify(self.title) + '_' + slugify_date(str(datetime.now()))

    def __repr__(self):
        return '<Products %r, id: %r>' % (self.title, self.id)

class Tag(db.Model):
    """
    Таблица 
    """
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100))
    name = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '<Tag %r, id: %r>' % (self.name, self.id)

class Maintable(db.Model):
    __tablename__ = 'maintable'
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(150), unique=True)
    created = db.Column(db.DateTime, default=datetime.now())
    section = db.Column(db.String(100))
    link = db.Column(db.String(100))
    title_page = db.Column(db.String(100))
    name_link = db.Column(db.String(100))
    data_page = db.Column(db.Text)

    id_articles = db.relationship('Articles', backref='maintable', lazy='dynamic')
    id_products = db.relationship('Products', backref='maintable', lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super(Maintable, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name_link)

    def __repr__(self):
        return '<Maintable section:%r, link: %r, title_page: %r, name_link: %r>' % (self.section, self.link, self.title_page,  self.name_link)

roles_users = db.Table('roles_users',
            db.Column('user_id',db.Integer, db.ForeignKey('user.id')),
            db.Column('role_id',db.Integer, db.ForeignKey('role.id')))



class User (db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())

    roles = db.relationship('Role', secondary=roles_users ,backref=db.backref('userus', lazy='dynamic'))
    

    def __repr__(self):
        return '<User: %r,%r>' % (self.username, self.email)

class Role(db.Model,RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy='dynamic')

    users = db.relationship('User', secondary=roles_users,backref=db.backref('roleus', lazy='dynamic'))
    
    def __repr__(self):
        return '<Role %r>' % self.name


