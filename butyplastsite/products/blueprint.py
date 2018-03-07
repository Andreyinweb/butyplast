from flask import Blueprint, render_template, request, redirect, url_for
from app import db

from models import Products


products = Blueprint('products', __name__, template_folder='templates')

@products.route('/')
def index():
    menu = True
    products_db = Products.query.all()
    return render_template('products/index.html', menu=menu, products_db=products_db)

@products.route('/<slug>')
def product(slug):
    menu = True
    products_db  = Products.query.filter_by(slug=slug).first()
    
    return render_template('products/product.html', menu=menu, products_db=products_db)
    
