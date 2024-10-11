from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

class UserForm(FlaskForm):
    """Form for adding users."""
    
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class TweetForm(FlaskForm):
    """Form for adding tweets."""
    
    text = StringField('Tweet',  validators=[InputRequired()])