from flask import Blueprint, render_template, request, redirect, url_for
from app import db

from models import Articles


from .forms import AddArticlesForm

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

@articles.route('/add', methods=['GET', 'POST'])
def add():
    form = AddArticlesForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_article = Articles(title=form.title.data, body=form.body.data, specification=form.specification.data)
            new_article.id_main = 3
            # Добавляет в сессию базы данных
            db.session.add(new_article)
                # Сохраняет  сессию базы данных.
            try:
                db.session.commit()
                message = "  успешно добавленно."
                form.title.data = ''
                form.body.data = ''
                form.specification.data = ''
                link = "/articles/" + new_article.slug
                print(link)
                return render_template("articles/add.html", form=form, message=message, link=link)   
            except :
                message = "НЕ СОХРАНИЛОСЬ"
                return render_template("articles/add.html", form=form, message=message)

    return render_template("articles/add.html", form=form)