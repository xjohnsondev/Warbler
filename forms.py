from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, EmailField
from wtforms.validators import DataRequired,InputRequired, Email, Length


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL')


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])

 
class UserDetailsForm(FlaskForm):
    """Update User Details"""

    username = StringField('Username')
    email = EmailField('Email', validators=[Email("Please enter a valid email")])
    location = StringField('Location')
    bio = StringField('Bio')       
    image_url = StringField('Image URL')
    header_img = StringField('Header Image URL')
    password = PasswordField('', validators=[InputRequired("Incorrect Password")])