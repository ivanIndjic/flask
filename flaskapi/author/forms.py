from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, EmailField
import email_validator


class RegisterForm(FlaskForm):
    full_name = StringField('Full Name', [validators.InputRequired()])
    email = EmailField('Email', [validators.Email(), validators.InputRequired()])
    password = PasswordField('Password', [validators.InputRequired(),
                                          validators.Length(min=4, max=40)])

    confirm = PasswordField('Repeat Password',
                            [validators.EqualTo('password', message='Passwords must match')])
