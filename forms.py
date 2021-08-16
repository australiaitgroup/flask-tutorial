from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    title = StringField('Title of Post:', validators=[DataRequired()])
    content = TextAreaField('Content of Post:', validators=[DataRequired()])
    featured = BooleanField('Is featured')
    submit = SubmitField('Submit Post')
