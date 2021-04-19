from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

#email, passwordm submit_button
class UserLoginform(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators = [DataRequired()])
    submit_button=SubmitField()
