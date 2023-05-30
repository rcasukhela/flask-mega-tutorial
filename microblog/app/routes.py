from flask import render_template
from app import app

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