from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(120))
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    '''
    The User class created above inherits from db.Model, a base class
    for all models from Flask-SQLAlchemy. This class defines several fields
    as class variables.
    
    Fields are created as instances of the db.Column class, which takes the
    field type as an argument, plus other optional arguments that, for example,
    allow us to indicate which fields are unique and indexed, which is important
    so that database searchers are efficient.
    
    The __repr__ method tells Python how to print objects of this class,
    which will be useful for debugging. Example:
    
    >>> from app.models import User
    >>> u = User(username='susan', email='susan@example.com')
    >>> u
    <User susan>
    
    
    '''