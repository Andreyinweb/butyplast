from flask import Blueprint, render_template, request, redirect, url_for
from app import db

# Название которое используется в ссылках, текущее имя, папка с шаблонами
goods = Blueprint('goods', __name__, template_folder='templates')


@goods.route('/')
def index():
    menu = True
    product_db = None
    return render_template('goods/index.html', menu = menu, product_db=product_db)