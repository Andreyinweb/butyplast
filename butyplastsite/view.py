from app import app
from flask import render_template



@app.route('/')
def lending():
    menu = False
    # Uncomment if you want to display a variable. Раскомментировать если нужно вывести на экран переменную.
    # message = Markup('<nav class="navbar navbar-inverse"><div class="container-fluid"><div class="navbar-header"><button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar"><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span></button></div><div class="collapse navbar-collapse" id="myNavbar"><ul class="nav navbar-nav"><li class="active"><a href="https://butyplast.com">Главная</a></li><li><a href="https://butyplast.com/about_us">О нас</a></li><li><a href="https://butyplast.com/g4182743-materialy-dlya-vibroizolyatsii">Товары</a></li><li><a href="https://butyplast.com/contacts">Контакты</a></li></ul></div></div></nav>')
    return render_template("index.html", menu = menu) # , message = message Paste if you want to display a variable. Вставить если нужно вывести на экран переменную.

@app.route('/index')
def index():
    menu = False
    return render_template("index.html", menu = menu)


@app.route('/buy')
def buy():
    menu = True
    product_db = Product.query.filter_by(page = "buy").all()
    return render_template("buy.html",product_db = product_db, menu = menu)

@app.route('/details')
def details():
    menu = True
    product_db = Product.query.filter_by(page = "details").all()
    return render_template("details.html",product_db = product_db, menu = menu)

@app.route('/installation')
def installation():
    menu = True
    product_db = Product.query.filter_by(page = "installation").all()
    return render_template("installation.html",product_db = product_db, menu = menu)




@app.route('/about')
def about():
    menu = True
    product_db = Product.query.filter_by(page = "about").all()
    return render_template("about.html",product_db = product_db, menu = menu)

@app.route('/contacts')
def contacts():
    menu = True
    product_db = Product.query.filter_by(page = "contacts").all()
    return render_template("contacts.html",product_db = product_db, menu = menu)