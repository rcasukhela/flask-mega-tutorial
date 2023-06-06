# The application will exist in a package.

# In Python, a sub-directory that includes an __init__.py file
# is considered a package, and can be imported.

# When you import a package, the __init__.py file
# executes and defines what symbols the package exposes
# to the outside world.

from flask import Flask

# Read the config file.
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Apply the config file.
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

# The logic above, creates the application object,
# as an instance of the class Flask, imported
# from the flask package.

# The variable __name__ is a Python 
# pre-defined variable.

# Flask uses the location of the module passed
# here as a starting point when it needs
# to load associated resources such as template files,
# which will be covered in Chapter 2.
# For practical purposes, passing __name__ will
# usually work.

# The application imports the module routes,
# which doesn't exist yet.

# Note that the module routes is imported
# at the bottom and not at the top of the script,
# as is usually done. This is a workaround to circular
# imports, and I'll just leave it at that because
# the rest of that explanation is confusing the hell
# out of me.

# The module routes contains the different URLs that
# the application implements.

# In Flask, handlers for the routes (or URLs) are written as Python
# functions, called 'view functions'.

# View functions are mapped to one or more route URLs
# so that Flask knows what logic to execute when a client
# requests a given URL.

# We write the first view function for this application in
# app/routes.py.

'''
We have made three changes to the init script. First, we have added a db object
that represents the database. Then we have added another object that
represents the migration engine.

There is a pattern beginning to develop in how to work with Flask extensions:
typically, we need to initialize extensions here in the __init__.py file.

Finally, we import a new module called models at the bottom, which will
define the structure of the database.
'''