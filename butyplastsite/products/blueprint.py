from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from models import Products
from programs.pagination import Pagination


products = Blueprint('products', __name__, template_folder='templates')


@products.route('/')
def index():

    per_page = 5  # Количество результатов на странице
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    # Sorting list
    sort = {'по дате: новые': Products.created.desc(),
            'от дешевых к дорогим': Products.price.asc(),
            'от дорогих к дешевым': Products.price.desc(),
            'по дате: старые': Products.created.asc()}
    sorts = [s for s in sort]
    # Sorting method
    sorting = request.args.get('sorting')
    # If not sorting
    if not sorting:
        sorting = 'по дате: старые'

    products_db = Products.query.order_by(sort[sorting]).all()

    total_count = len(products_db)
    pages = Pagination(page, per_page, total_count, products_db)

    return render_template('products/index.html', sorting=sorting, sorts=sorts, pages=pages)


@products.route('/<slug>')
def product(slug):

    products_db = Products.query.filter_by(slug=slug).first()
    # Return
    return render_template('products/product.html', products_db=products_db)
