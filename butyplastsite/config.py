from flask import redirect, request, session, url_for
from functools import wraps



# site page admin
site_page =('buy', 'details', 'installation')
page_now = 'buy'

SESSION_uid = {'uid': 1,'username': None}

UPLOAD_FOLDER = '/home/stariy/project/butyplast/site/mysite/static/uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'gif', 'png'])
SECRET_KEY = "secret_key"
SQLALCHEMY_DATABASE_URI = "sqlite:///butyplast.db"

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


as45dfgh56dfgdf = "admin"
dfxd5d5667fg767 = "admin"

