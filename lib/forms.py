from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField('Zadanie', validators=[DataRequired()])
    description = TextAreaField('Opis', validators=[DataRequired()])
    done = BooleanField('Zrobione tak/nie')
     
    