from flask import Flask, url_for
from config import Configuretion
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)

app.config.from_object(Configuretion)


db = SQLAlchemy(app)

# migrate = Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)


# admin = Admin(app)
# from models import *

# admin.add_view(ModelView(Post_user, db.session))
# admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Role, db.session))
# admin.add_view(ModelView(Tag, db.session))