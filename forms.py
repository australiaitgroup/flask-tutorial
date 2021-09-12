from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed


class AddForm(FlaskForm):
    title = StringField('Title of Post:', validators=[DataRequired()])
    author = StringField('Author of Post:', validators=[DataRequired()])
    content = TextAreaField('Content of Post:', validators=[DataRequired()])
    featured = BooleanField('Is featured')
    banner_image = FileField('Banner Image:', validators=[
                             FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit Post')


class UpdateForm(FlaskForm):
    title = StringField('Title of Post:', validators=[DataRequired()])
    author = StringField('Author of Post:', validators=[DataRequired()])
    content = TextAreaField('Content of Post:', validators=[DataRequired()])
    banner_image = FileField('Banner Image:', validators=[
        FileAllowed(['jpg', 'png'])])
    featured = BooleanField('Is featured')
    submit = SubmitField('Submit Post')


class DeleteForm(FlaskForm):
    id = IntegerField('Id Number of Post to Remove:')
    submit = SubmitField('Remove Post')
