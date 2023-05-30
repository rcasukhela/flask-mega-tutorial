# The application will exist in a package.

# In Python, a sub-directory that includes an __init__.py file
# is considered a package, and can be imported.

# When you import a package, the __init__.py file
# executes and defines what symbols the package exposes
# to the outside world.

from flask import Flask

app = Flask(__name__)

from app import routes

