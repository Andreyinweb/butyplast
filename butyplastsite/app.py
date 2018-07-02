from flask import Flask, url_for
from config import Configuretion
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


from flask_security import SQLAlchemyUserDatastore, Security


# from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager



app = Flask(__name__)

app.config.from_object(Configuretion)


db = SQLAlchemy(app)

# migrate = Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)




admin = Admin(app) # , endpoint='index'
from models import Articles, Products, Maintable , Tag, Role, User 


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(Articles, db.session, endpoint='Article'))
admin.add_view(ModelView(Products, db.session, endpoint='Product'))
admin.add_view(ModelView(Tag, db.session))
admin.add_view(ModelView(Maintable, db.session))


#### flask_security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
