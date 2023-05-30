from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' +user['username']+'''.</h1>
    </body>
</html>
'''

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