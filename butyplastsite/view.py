from app import app
from flask import render_template, request #, redirect, url_for
from models import Articles, Goods


@app.route('/')
def index():
    menu = False
    # Uncomment if you want to display a variable. Раскомментировать если нужно вывести на экран переменную.
    # message = Markup('<nav class="navbar navbar-inverse"><div class="container-fluid"><div class="navbar-header"><button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar"><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span></button></div><div class="collapse navbar-collapse" id="myNavbar"><ul class="nav navbar-nav"><li class="active"><a href="https://butyplast.com">Главная</a></li><li><a href="https://butyplast.com/about_us">О нас</a></li><li><a href="https://butyplast.com/g4182743-materialy-dlya-vibroizolyatsii">Товары</a></li><li><a href="https://butyplast.com/contacts">Контакты</a></li></ul></div></div></nav>')
    return render_template("index.html", menu = menu) # , message = message Paste if you want to display a variable. Вставить если нужно вывести на экран переменную.


@app.route('/about')
def about():
    menu = True
    product_db = None
    return render_template("about.html",product_db = product_db, menu = menu)

@app.route('/contacts')
def contacts():
    menu = True
    product_db = None
    return render_template("contacts.html",product_db = product_db, menu = menu)

@app.route('/search')
def search():
    menu = True
    # page = request.args.get('page')

    # if page and page.isdigit():
    #     page = int(page)
    # else:
    #     page = 1
    
    
    q = request.args.get('q')

    if q:
        search_db1 = Goods.query.filter(Goods.title.contains(q) | Goods.body.contains(q) | Goods.specification.contains(q)).all()
        search_db2 = Articles.query.filter(Articles.title.contains(q) | Articles.body.contains(q) | Articles.specification.contains(q)).all()        
        search_db = {'goods.product':search_db1, 'articles.more_info': search_db2}
        message = "По запросу: " + q + "     ---------  Hайдено :  " + str(len(search_db1) + len(search_db2)) + "  результатов."
        if  not search_db:
            search_db = Goods.query.all()
            message = "По запросу: " + q + "   ничего не найдено!"    

    else:
        search_db = Goods.query.order_by(Goods.created.desc())
        message = ""

    # pages = posts.paginate(page=page, per_page=7)

    return render_template("search.html", menu=menu, message=message, search_db=search_db)