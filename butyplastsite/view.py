from app import app, db
from flask import render_template, request, url_for, redirect
from models import *
from programs.pagination import Pagination


@app.route('/')
def index():
    # Home page
    return render_template("index.html") 


@app.route('/about')
def about():
    # 
    return render_template("about.html")


@app.route('/contacts')
def contacts():
    return render_template("contacts.html")


@app.route('/search')
def search():
    # Number of results per page
    # Количество результатов на странице
    per_page = 10  
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    # Sorting list
    sort = {'по дате: старые': [Products.created.desc(), Articles.created.desc()],
            'от дешевых к дорогим': [Products.price.asc(), Articles.created.asc()],
            'от дорогих к дешевым': [Products.price.desc(), Articles.created.asc()],
            'по дате: новые': [Products.created.asc(), Articles.created.asc()] }
    sorts =[s for s in sort]
    # Sorting method
    sorting = request.args.get('sorting')
    if not sorting:
        sorting = 'по дате: старые'
    
    q = request.args.get('q')

    if q:
        # Search in the table Products
        search_db1 = Products.query.order_by(sort[sorting][0]).filter( Products.title.contains(q) |
                                    Products.body.contains(q) | Products.specification.contains(q)).all()
        # Search in the table Articles
        search_db2 = Articles.query.order_by(sort[sorting][1]).filter(Articles.title.contains(q) |
                                    Articles.body.contains(q) | Articles.specification.contains(q)).all()
        # Join search
        search_db = search_db1 + search_db2
        if  search_db :                          
            message = "По запросу: ____ " + q + " __________ Hайдено :  " + str(len(search_db)) + "  совпадений."
        else :
            # Splits into words and removes the endings
            #  Делит на слова и удаляем окончания
            words = q.split()
            for q1 in words:
                if len(q1) > 5 : q1 = q1[0:-3]
                # Search in the table Products
                search_db1 = Products.query.order_by(sort[sorting][0]).filter( Products.title.contains(q1) |
                                            Products.body.contains(q1) | Products.specification.contains(q1)).all()
                # Search in the table Articles
                search_db2 = Articles.query.order_by(sort[sorting][1]).filter(Articles.title.contains(q1) |
                                            Articles.body.contains(q1) | Articles.specification.contains(q1)).all()
                # Join search
                search_db = search_db1 + search_db2
                if  search_db :
                    message = "По запросу: ____ " + q + " __________ Hайдено :  " + str(len(search_db)) + "  совпадений."
                
            if  not search_db:
                search_db = Products.query.order_by(sort[sorting][0]).all() + Articles.query.order_by(sort[sorting][1]).all()
                message = "По запросу: ____ " + q + " __________ ничего не найдено!"    

    else:
        # If not found, returns a list of products
        search_db = Products.query.order_by(sort[sorting]).all()
        message = ""
    total_count = len(search_db)
    pages = Pagination(page, per_page, total_count, search_db)  
    # Search page
    return render_template("search.html", message=message,  sorting=sorting ,  sorts=sorts, pages=pages)
