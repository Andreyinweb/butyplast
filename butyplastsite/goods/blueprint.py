from flask import Blueprint, render_template, request, redirect, url_for
from app import db

from models import Goods


goods = Blueprint('goods', __name__, template_folder='templates')

@goods.route('/')
def index():
    menu = True
    goods_db = Goods.query.all()
    return render_template('goods/index.html', menu = menu, goods_db=goods_db)