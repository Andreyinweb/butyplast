from flask import Blueprint, render_template, request, redirect, url_for
from app import db

from models import Articles

# Название которое используется в ссылках, текущее имя, папка с шаблонами
articles = Blueprint('articles', __name__, template_folder='templates')

@articles.route('/')
def index():
    menu = True
    article_db = Articles.query.all()
    return render_template('articles/index.html', menu=menu, article_db=article_db)

    more_info
@articles.route('/<slug>')
def more_info(slug):
    menu = True
    articles_db  = Articles.query.filter_by(slug=slug).first()
    
    return render_template('articles/more_info.html', menu=menu, articles_db=articles_db)