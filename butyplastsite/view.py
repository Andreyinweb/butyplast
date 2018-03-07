from app import app
from flask import render_template, request, url_for #, redirect
from models import Articles, Products, Maintable
from programs.pagination import Pagination

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
    per_page = 3 # Количество результатов на странице 
    
    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    sort = {'по дате: старые': [Products.created.desc(), Articles.created.desc()],
            'от дешевых к дорогим': [Products.price.asc(), Articles.created.asc()],
            'от дорогих к дешевым': [Products.price.desc(), Articles.created.asc()],
            'по дате: новые': [Products.created.asc(), Articles.created.asc()] }
    sorts =[s for s in sort]

    sorting = request.args.get('sorting')
    if not sorting:
        sorting = 'по дате: старые'
    
    q = request.args.get('q')

    if q:
        
        search_db1 = Products.query.order_by(sort[sorting][0]).filter( Products.title.contains(q) |
                                    Products.body.contains(q) | Products.specification.contains(q)).all()

        search_db2 = Articles.query.order_by(sort[sorting][1]).filter(Articles.title.contains(q) |
                                    Articles.body.contains(q) | Articles.specification.contains(q)).all()
        
        search_db = search_db1 + search_db2
        if  search_db != 0:                          
            message = "По запросу: ____ " + q + " __________ Hайдено :  " + str(len(search_db)) + "  совпадений."
        else :
            # Делим на слова и удаляем окончания
            words = q.split()
            for q1 in words:
                if len(q1) > 5 : q1 = q1[0:-3]
                search_db1 = Products.query.order_by(sort[sorting]).filter(Products.title.contains(q1) | Products.body.contains(q1) | Products.specification.contains(q1)).all()
                search_db2 = Articles.query.filter(Articles.title.contains(q1) | Articles.body.contains(q1) | Articles.specification.contains(q1)).all()        
                search_db = {'products.product':search_db1, 'articles.more_info': search_db2}
                message = "По запросу: ____ " + q + " __________ Hайдено :  " + str(len(search_db1) + len(search_db2)) + "  совпадений."
                
            if  not search_db1:
                search_db = {'products.product': Products.query.order_by(sort[sorting])}
                message = "По запросу: ____ " + q + " __________ ничего не найдено!"    

    else:
        search_db = Products.query.order_by(sort[sorting])
        message = ""
    total_count = len(search_db)
    pagination = Pagination(page, per_page, total_count)   
    list_out = pagination.list_paginat(search_db)
    pages = pagination

    # pages = None
    # print(dir(search_db1))

    return render_template("search.html", menu=menu, message=message, list_out=list_out, sorting=sorting ,  sorts=sorts, pages=pages)

