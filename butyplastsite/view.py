from app import app
from flask import render_template



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