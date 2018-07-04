from flask import Blueprint, render_template, request, redirect, url_for
from app import app, db
from models import Articles
import os
from programs.pagination import Pagination

# Название которое используется в ссылках, текущее имя, папка с шаблонами
articles = Blueprint('articles', __name__, template_folder='templates')

@articles.route('/')
def index():
    menu = True
    per_page = 5 # Количество результатов на странице
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    sort = {'по дате: новые': Articles.created.desc(),
            'по дате: старые': Articles.created.asc()}
    sorts =[s for s in sort]
    sorting = request.args.get('sorting')

    if not sorting:
        sorting = 'по дате: новые'

    article_db = Articles.query.order_by(sort[sorting]).all()

    total_count = len(article_db)
    pages = Pagination(page, per_page, total_count, article_db)

    return render_template('articles/index.html', menu=menu, sorting=sorting,  sorts=sorts, pages=pages)

@articles.route('/<slug>')
def more_info(slug):
    menu = True
    articles_db  = Articles.query.filter_by(slug=slug).first()

    return render_template('articles/more_info.html', menu=menu, articles_db=articles_db)

