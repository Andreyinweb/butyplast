from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SubmitField
from wtforms.validators import DataRequired


from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired


class AddArticlesForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    body = TextAreaField('Короткое описание', validators=[DataRequired()])
    specification = TextAreaField('Описание', validators=[DataRequired()])
    upload =  FileField('Фото', validators=[FileRequired()])

    submit = SubmitField("Сохранить")
    # nosubmit = SubmitField("He oтправить")
