import os

'''
During development, we are going to use a SQLite database. SQLite databases
are the most convenient choice for developing small applications, as each
database is stored in a single file on disk and there is no need to run a
database server like MySQL and PostgreSQL.

We add two new configuration items to the config file.
'''

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    '''
    The Flask-SQLAlchemy extension takes the location of the application's
    database from the SQLALCHEMY_DATABASE_URI configuration variable.
    
    In general, it is good practice to set configuration from environment
    variables, and provide a fallback value when the environment does not define
    the variable. In this case I'm taking the database URL from the
    DATABASE_URL environment variable, and if that isn't defined, I'm
    configuring a database named app.db located in the main directory of the
    application, which is stored in the basedir variable.
    
    The SQLALCHEMY_TRACK_MODIFICATIONS configuration option is set to False
    to disable a feature of Flask-SQLAlchemy that sends a signal to the
    application every time a change is about to be made in the database.
    
    The database is going to be represented in the application by the database
    instance. The database migration engine will also have an instance. These
    are objects that need to be created after the application, in the
    app/__init__.py file.
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
# The configuration settings are defined as class variables inside the Config
# class. As the application needs more configuration items, they can be added
# to this class.

# Later, if we find that we need to have more than one configuration set,
# we may create subclasses of it. However, we do not concern ourselves with this
# just yet.

# The SECRET_KEY config vairable is important for most Flask applications,
# using it to generate signatures or tokens.
# In particular, the Flask-WTF extension uses it to protect web forms against
# Cross-Site Request Forgery (CSRF) attacks.

# We use an OR statement to define the secret key because we just need to bypass
# the first of the logic: we'd like the secret key to be sourced from an 
# actual environmental variable of the operating system.
# In testing, a hardcoded string is fine, but in production,
# we need to set a unique and difficult to guess value in the environment,
# so that the server has a secure key that nobody else knows.

# Now that we have a config file, we need to tell Flask to read and apply it.
# We go to __init__.py and apply this logic: