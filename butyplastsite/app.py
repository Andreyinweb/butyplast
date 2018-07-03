from flask import Flask, url_for, redirect, request
from config import Configuretion
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView


from flask_security import SQLAlchemyUserDatastore, Security, current_user


# from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager



app = Flask(__name__)

app.config.from_object(Configuretion)



db = SQLAlchemy(app)

# migrate = Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)



class AdminView(ModelView):
    def is_accessible(self):
        return current_user.has_role('Admin')

    def inaccessible_callback(self, name,**kwargs):
        return redirect(url_for('security.login', next=request.url))

class HomeAdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.has_role('Admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))
    
admin = Admin(app, 'Главная', url='/', index_view=HomeAdminView(name='Home'))
 # , endpoint='index'
from models import Articles, Products, Maintable , Tag, Role, User 


admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Role, db.session))
admin.add_view(AdminView(Articles, db.session, endpoint='Article'))
admin.add_view(AdminView(Products, db.session, endpoint='Product'))
admin.add_view(AdminView(Tag, db.session))
admin.add_view(AdminView(Maintable, db.session))

#### flask_security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

