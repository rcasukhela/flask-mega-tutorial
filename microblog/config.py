import os

class Config(object):
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