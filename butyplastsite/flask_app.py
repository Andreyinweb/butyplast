# https://andreyinweb.pythonanywhere.com/

import os
# from config import *
from flask import Flask,  redirect, render_template, request, session, url_for
# from  flask  import  Markup
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from functools import wraps


#######################################################################################



#site page admin
site_page =('buy', 'details', 'installation')
page_now = 'buy'

SESSION_uid = {'uid': 1,'username': None}

UPLOAD_FOLDER = '/home/stariy/andrey/butyplast/site/butyplastsite/static/uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'gif', 'png'])
SECRET_KEY = "secret_key"
SQLALCHEMY_DATABASE_URI = "sqlite:///butyplast.db"

as45dfgh56dfgdf = "admin"
dfxd5d5667fg767 = "admin"

###########################################################################

#
app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


db = SQLAlchemy(app)

#####################################################

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.11/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("uid") != 28965:
            return redirect(url_for("login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

#########################################################################################

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    page = db.Column(db.String(20))
    image = db.Column(db.String(100))
    heading = db.Column(db.String(100))
    text = db.Column(db.String(500))
    price = db.Column(db.Float)
    link = db.Column(db.String(100))
db.create_all()



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

@app.route("/login", methods=["GET", "POST"])
def login():
#     """Log user in."""
    menu = True
    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            message = "Поле логин не должно быть пустым"
            return render_template("login.html",message = message, menu = menu)
         # ensure password was submitted
        elif not request.form.get("password"):
            message = "Поле пароль не должно быть пустым"
            return render_template("login.html",message = message, menu = menu)
        if request.form.get("username") == as45dfgh56dfgdf and request.form.get("password") == dfxd5d5667fg767 :
            if session or not session:
        # # remember which user has logged in
                qwer = 28965
                session['uid'] = qwer
                session['username'] = "admin"
                return redirect(url_for("admin"))
        else:
            message = "Неправильный логин или пароль"
            return render_template("login.html",message = message, menu = menu)
        # redirect user to admin
        return redirect(url_for("admin"))


    # else if user reached route via GET (as by clicking a link or via redirect)

    message = "Введите логин и пароль"
    return render_template("login.html",message = message, menu = menu)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    #     """Log user in."""
    session['uid'] = 1
    return redirect(url_for("login") )

@app.route('/admin', methods=["GET", "POST"])
@login_required
def admin():
    global site_page
    global page_now
    # search for unused id
    y = list()
    product_db = Product.query.order_by(Product.id).all()
    if product_db != []:
        for z in product_db:
            y.append(z.id)
        z =[x for x in range(1, product_db[-1].id)]
        new_id= list(set(z) - set(y))
    else :
        new_id = None

    if request.method == "POST":



        if request.form.get("change_page"):
            page_now = request.form.get("page_now")
            product_db = Product.query.filter_by(page = page_now).all()
            return render_template("admin.html",product_db = product_db, new_id = new_id, site_page = site_page, page_now = page_now)

        if request.form.get("price") and is_number(request.form.get("price")):
            price = float(request.form.get("price"))
        else:
            price = 0.0

        if request.form.get("id") != None:
            id_q = int(request.form.get("id"))



            #  FILE
            if 'file' in request.files:



                file = request.files['file']



                # if user does not select file, browser also
                # submit a empty part without filename
                if file.filename != '':



                    if file and allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                        product_db = Product.query.filter_by(id = id_q).first()
                        db.session.delete(product_db)
                        db.session.commit()
                        new_product = Product( id=product_db.id, image = filename , page = page_now, heading = request.form.get("heading"), text = request.form.get("textarea"), price = price, link = request.form.get("link"))
                        db.session.add(new_product)
                        db.session.commit()
                else:


                    product_db = Product.query.filter_by(id = id_q).first()
                    page_now = product_db.page



                    db.session.delete(product_db)
                    db.session.commit()

                    new_product = Product( id=product_db.id, image = product_db.image, page = page_now, heading = request.form.get("heading"), text = request.form.get("textarea"), price = price, link = request.form.get("link"))

                    db.session.add(new_product)
                    db.session.commit()
        #### DELETE #####
        elif request.form.get("del") != None:


            id_q = int(request.form.get("del"))
            product_db = Product.query.filter_by(id = id_q).first()



            page_now = product_db.page


            if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], product_db.image)) :
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], product_db.image))

            db.session.delete(product_db)
            db.session.commit()


    product_db = Product.query.filter_by(page = page_now).all()
    return render_template("admin.html",product_db = product_db, new_id = new_id, site_page = site_page, page_now = page_now)

@app.route('/new_product', methods=["GET", "POST"])
@login_required
def new_product():

    if request.method == "POST":
        if request.form.get("price") and is_number(request.form.get("price")):
            price = float(request.form.get("price"))
        else:
            price = 0.0

        #  FILE
        if 'file' in request.files:
            file = request.files['file']
            # if user does not select file, browser also
            # submit a empty part without filename

            if file.filename != '':
                if file and allowed_file(file.filename):

                    # message = str(allowed_file(file.filename))  #del
                    # return render_template("index.html", message = message) #del

                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                else:
                    filename = "not.png"
            else:
                filename = "not.png"

        else:
            filename = "not.png"

        if request.form.get("select") != '' and request.form.get("select") != None :
            new_product = Product(id = int(request.form.get("select")), image = filename , page = page_now, heading = request.form.get("heading"), text = request.form.get("textarea"), price = price, link = request.form.get("link"))
            db.session.add(new_product)
            db.session.commit()
        else :
            new_product = Product(image = filename , page = page_now, heading = request.form.get("heading"), text = request.form.get("textarea"), price = price, link = request.form.get("link"))
            db.session.add(new_product)
            db.session.commit()

    return redirect('/admin')

