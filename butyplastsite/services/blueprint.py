from flask import Blueprint, render_template, request, redirect, url_for
from app import db

# Название которое используется в ссылках, текущее имя, папка с шаблонами
services = Blueprint('services', __name__, template_folder='templates')

@services.route('/')
def index():
    menu = True
    product_db = None
    return render_template('services/index.html', menu = menu, product_db=product_db)