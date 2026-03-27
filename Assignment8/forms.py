# Flask-WTF for form:
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Length, Email

# Import the other py files required
from model import User

# WTF-FORMS
class LoginForm(FlaskForm):
    userid = StringField('User ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class UserDetails(FlaskForm):
    userid = StringField('User ID', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message='Invalid Email Address')])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=8, max=15, message='Phone Number must be between 8 and 15 characters')])
    city = StringField('City', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=15, message='Password must be between 8 and 15 characters')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message = "Password Must Match!")])
    submit = SubmitField('Register')

    def validate_userid(self, userid):
        user = User.query.filter_by(userid=userid.data).first()
        print(f"This is user {user}")
        if user:
            raise ValidationError('This User ID is already taken.')





