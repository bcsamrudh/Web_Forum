from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class CommentForm(FlaskForm):
    comment = StringField('comment', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    desc= StringField('desc', validators=[DataRequired()])
    submit = SubmitField('Create')