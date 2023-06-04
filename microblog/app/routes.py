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
    This is because we have no logic to process any data submitted by the user.
    
    The form.validate_on_submit() method does the form processing work.
    When the browser sends the GET request to receive the web page with the
    form, form.validate_on_submit() will return False. So in that case,
    the function skips the if statement and goes directly to render the
    template in the last line of the function:
    
        return render_template('login.html', title='Sign In', form=form)
        
    When the browser sends the POST request as a result of the user pressing
    the submit button, form.validate_on_submit() will gather all the
    data, and run all the validators attached to fields. If everything is all
    right it will return True. This indicates that the data is valid and can
    be processed by the application. If at least one field fails validation,
    the function will return False, and that will cause the form to be
    rendered back to the user, like in the GET request case.
    
    Later, we will add an error message when validation fails.
    '''
    form = LoginForm()
    
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username_data}, \
              remember_me={form.remember_me.data}')
        '''
        When form.validate_on_submit() returns True, the login view function calls
        two new functions, imported from Flask.
        The flash() function is a useful way to show a message to the user.
        Many applications use flash() to let the user know if some action has been
        successful or not. In this case, we use the function flash() as a
        temporary solution, because we do not have the infrastructure necessary to
        log users in properly yet. The best we can do for now is to show a message
        that confirms that the application properly received the credentials.
        
        When we call the flash() functiono, Flask stores the message, but
        flashed messages will not magically appear in web pages. The templates
        oof the application neede to render these flashed messages in a way
        that is conformant with the site layout.
        
        We will add these messages to the template base.html, so that all
        templates will inherit this functionality.
        '''
        return redirect('/index')
    '''
    The second new function used in the login view is redirect(). This function
    instructs the client web browser to automatically navigate to a different
    page, given as an argument.
    
    This view function uses it to redirect the user to the index page of the
    application.
    '''
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