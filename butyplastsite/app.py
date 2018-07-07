from flask import Flask, url_for, redirect, request
from config import Configuretion
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView, form
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore, Security, current_user
import os.path as op
from sqlalchemy.event import listens_for
from jinja2 import Markup
from flask_admin.form import rules
from flask_admin.contrib import sqla

app = Flask(__name__)

app.config.from_object(Configuretion)
############################################################################################################################
db = SQLAlchemy(app)

####### ADMIN ######
file_path = app.config['UPLOAD_FOLDER']

from models import *


@listens_for(Articles, 'after_delete')
def del_image(mapper, connection, target):
    """Image"""

    if target.path:
        # Delete image
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass

        # Delete thumbnail
        try:
            os.remove(op.join(file_path,
                              form.thumbgen_filename(target.path)))
        except OSError:
            pass


class ImageView(sqla.ModelView):
    """ImageView """

    def _list_thumbnail(view, context, model, name):
        if not model.image:
            return ''
        return Markup('<img src="%s">' % url_for('static',
                                                 filename='uploads/' + form.thumbgen_filename(model.image)))

    column_formatters = {
        'image': _list_thumbnail
    }

    # Alternative way to contribute field is to override it completely.
    # In this case, Flask-Admin won't attempt to merge various parameters for the field.
    form_extra_fields = {
        'image': form.ImageUploadField('Image',
                                       base_path=file_path,
                                       thumbnail_size=(100, 100, True))
    }


###################################################################################################################################
class AdminMixin:
    """Admin Mixin """

    def is_accessible(self):
        return current_user.has_role('Admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class BaseModelView(ModelView):
    """Base Model View"""

    def on_model_change(self, form, model, is_created):
        print(model.generate_slug())
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


###########################################################################################
class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


class ArticlesAdminView(AdminMixin, BaseModelView, ImageView):
    form_columns = ['title', 'body', 'specification', 'image', 'id_main']


class ProductsAdminView(AdminMixin, BaseModelView, ImageView):
    form_columns = ['title', 'body', 'specification', 'price', 'image', 'id_main']


##############################################################################################################
# Admin conect
admin = Admin(app, 'Главная',  url='/', index_view=HomeAdminView(name='Администрирование'))

admin.add_view(ArticlesAdminView(Articles, db.session, name='Описание', endpoint='Article'))
admin.add_view(ProductsAdminView(Products, db.session, name='Товары', endpoint='Product'))
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Role, db.session))

###################################################################################################################
# flask_security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
