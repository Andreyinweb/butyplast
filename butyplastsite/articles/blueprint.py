from flask import Blueprint, render_template, request, redirect, url_for
from app import app, db
from models import Articles
from flask_security import login_required 
from .forms import AddArticlesForm
import os
from werkzeug.utils import secure_filename
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

    sort = {'по дате: старые': Articles.created.desc(),
            'по дате: новые': Articles.created.asc()}
    sorts =[s for s in sort]
    sorting = request.args.get('sorting')

    if not sorting:
        sorting = 'по дате: старые'

    article_db = Articles.query.order_by(sort[sorting]).all()

    total_count = len(article_db)
    pages = Pagination(page, per_page, total_count, article_db)

    return render_template('articles/index.html', menu=menu, sorting=sorting,  sorts=sorts, pages=pages)

@articles.route('/<slug>')
def more_info(slug):
    menu = True
    articles_db  = Articles.query.filter_by(slug=slug).first()
    
    return render_template('articles/more_info.html', menu=menu, articles_db=articles_db)

@articles.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    menu = True
    form = AddArticlesForm()
    # upload_form = UploadForm()
    if request.method == "POST":
        if form.validate_on_submit():

            f = form.upload.data
            filename = secure_filename(f.filename)
        
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            new_article = Articles(title=form.title.data, body=form.body.data,
                                     specification=form.specification.data,
                                     image=("../static/uploads/" + filename))
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
                return render_template("articles/add.html", menu=menu, form=form, message=message, link=link)   
            except :
                message = "НЕ СОХРАНИЛОСЬ"
                return render_template("articles/add.html", menu=menu, form=form, message=message)

    return render_template("articles/add.html", menu=menu, form=form) #, upload_form=upload_form)