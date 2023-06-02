from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    # We can now simplify the view function, as the presentation of the page
    # has been offloaded to the HTML template. Note the structure of this
    # function: the first argument is the template name, index.html.
    # the second and third arguments are required to fill in the 
    # variables called out in the HTML file index.html.
    # The render_template() function invokes the Jinja2 template
    # engine that comes bundled with the Flask framework.
    # Jinja2 substitutes {{ ... }} 
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Here, we import the LoginForm class from the module forms.py. Then,
    we instantiate a LoginForm object, and send it to the template.
    
    Note the methods argument in the route decorator: This tells Flask
    that this view function accepts GET and POST requests, overriding the
    default, which is to accept only GET requests.
    
    The HTTP protocol states that GET requests are those that return
    information to the client. All the requests in the application so far
    are of this type. POST requests are typically used when the browser
    submits form data to the server.
    
    If the client attempts to submit a login request and the application was not
    configured to accept it, we would get a "Method Not Allowed" error.
    '''
    form = LoginForm()
    
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username_data}, \
              remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

# Chapter 1:
# The @app.route decorator creates an association between the URL
# given as an argument and the function.

# The two decorators associate the URLs '/' and '/index' to this
# function. What does this mean? When a web browser requests either
# of these two URLs, Flask is going to invoke index() and pass
# the return value of it back to the browser as a response.

# To complete the application we need to have a Python script at the
# top-level that defines the Flask application instance.
# We will call the script microblog.py, and define it as a single
# line that imports the application instance.

# From Chapter 2:
# Note that you can return raw HTML to the view, but this is not
# considered sustainable or good practice.

# If we can keep the logic of the application separate from the layout
# or presentation of the web pages, this will be far better. It also
# separates the front-end development and the back-end development
# a bit more.

# Templates help achieve this separation between the view logic and
# the business logic. In Flask, templates are written as separate files,
# stored in a templates folder that is inside the application package.