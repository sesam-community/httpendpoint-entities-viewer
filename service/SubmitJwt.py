from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class SubmitJwt(FlaskForm):
    jwt = TextAreaField('jwt', validators=[DataRequired()])
    submit = SubmitField('Submit')
