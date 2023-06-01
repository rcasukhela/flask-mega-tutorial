from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# The optional validators argument that you see in some of the fields
# is used to attach validation behaviors to fields.
# The DataRequired validator simply checks that the field is not submitted
# empty.
# Keep an eye out for other validators, some of which will be used in other
# forms.

# The next step is to add the form to an HTML template so that it can be
# rendered onto a web page.
# Fortunately, the fields that are defined in the LoginForm class know how to
# render themselves as HTML, so this not difficult.
# We will create the login template, which we will store in file
# app/templates/login.html