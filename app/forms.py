from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    title = StringField('Book Title')
    author = StringField('Author Name')
    subject = StringField('Subject')
    website = StringField('Website')
    submit = SubmitField('Search')