from datetime import datetime
from app import db

r'''
The model class created in the previous section defines the initial database
structure (or schema) for this application. But as the application continues
to grow, it is likely that I will need to make changes to that structure
such as adding new things, and sometimes to modify or remove items. Alembic
(the migration framework used by Flask-Migrate) will make these schema
changes in a way that does not require the database to be recreated from
scratch every time a change needs to be made.

To accomplish this seemingly difficult task, Alembic maintains a migration
repository, which is a directory in which it stores its migration scripts.
Each time a change is made to the database schema, a migration script is
added to the repository with the details of the change. To apply the
migrations to a database, these migration scripts are executed in the
sequence they were created.

Flask-Migrate exposes its commands through the flask command. You have
already seen flask run, which is a sub-command that is native to Flask.
The flask db sub-command is added by Flask-Migrate to manage everything
related to database migrations. So let's create the migration repository
for microblog by running flask db init:

(venv) (base) PS C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog> flask db init
Creating directory 'C:\\Users\\rcasu\\Documents\\demos\\flask-mega-tutorial\\microblog\\migrations' ...  done
Creating directory 'C:\\Users\\rcasu\\Documents\\demos\\flask-mega-tutorial\\microblog\\migrations\\versions' ...  done
Generating C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog\migrations\alembic.ini ...  done
Generating C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog\migrations\env.py ...  done
Generating C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog\migrations\README ...  done
Generating C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog\migrations\script.py.mako ...  done
Please edit configuration/connection/logging settings in 'C:\\Users\\rcasu\\Documents\\demos\\flask-mega-tutorial\\microblog\\migrations\\alembic.ini' before proceeding.

Remember that the flask command relies on the FLASK_APP environment variable
to know where the Flask application lives. For this application, you want to
set FLASK_APP to the value microblog.py, as discussed in Chapter 1.

After you run this command, you will find a new migrations directory, with a
few files and a versions sub-directory inside. All these files should be
treated as part of your project from now on, and in particular, should be
added to source control along with your application code.

With the migration repository in place, it is time to create the first
database migration, which will include the users table that maps to the User
database model. There are two ways to create a database migration: manually
or automatically. To generate a migration automatically, Alembic compares
the database schema as defined by the database MODELS, against the actual
database schema CURRENTLY USED in the database. It then populates the
migration script with the changes necessary to make the database schema
match the application models. In this case, since there is no previous
database, the automatic migration will add the entire User model to the
migration script. The flask db migrate sub-command generates these automatic
migrations:

(venv) (base) PS C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog> flask db migrate -m "users table"
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'user'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_user_email' on '['email']'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_user_username' on '['username']'
Generating C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog\migrations\versions\dd60320d0ec8_users_table.py ...  done

The output of the command gives you an idea of what Alembic included in the
migration. The first two lines are informational and can usually be ignored.
It then says that it found a user table and two indexes. Then it tells you
where it wrote the migration script. The e517276bb1c2 code is an
automatically generated unique code for the migration
(it will be different for you). The comment given with the -m option is
optional, it adds a short descriptive text to the migration.

The generated migration script is now part of your project, and needs to be
incorporated to source control. You are welcome to inspect the script if you
are curious to see how it looks. You will find that it has two functions
called upgrade() and downgrade(). The upgrade() function applies the
migration, and the downgrade() function removes it. This allows Alembic to
migrate the database to any point in the history, even to older versions, by
using the downgrade path.

The flask db migrate command does not make any changes to the database, it
just generates the migration script. To apply the changes to the database,
the flask db upgrade command must be used.

(venv) (base) PS C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog> flask db upgrade
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> dd60320d0ec8, users table

Because this application uses SQLite, the upgrade command will detect that a
database does not exist and will create it (you will notice a file named
app.db is added after this command finishes, that is the SQLite database).
When working with database servers such as MySQL and PostgreSQL, you have to
create the database in the database server before running upgrade.

Note that Flask-SQLAlchemy uses a "snake case" naming convention for
database tables by default. For the User model above, the corresponding
table in the database will be named user. For a AddressAndPhone model class,
the table would be named address_and_phone. If you prefer to choose your own
table names, you can add an attribute named __tablename__ to the model
class, set to the desired name as a string, like so:

class User(db.Model):
    ...
    __table__name = 'table_name'
    
The application is in its infancy at this point, but it does not hurt to
discuss what is going to be the database migration strategy going forward.
Imagine that you have your application on your development machine, and also
have a copy deployed to a production server that is online and in use.

Let's say that for the next release of your app you have to introduce a
change to your models, for example a new table needs to be added. Without
migrations you would need to figure out how to change the schema of your
database, both in your development machine and then again in your server,
and this could be a lot of work.

But with database migration support, after you modify the models in your
application you generate a new migration script (flask db migrate), you
probably review it to make sure the automatic generation did the right
thing, and then apply the changes to your development database
(flask db upgrade). You will add the migration script to source control and
commit it.

When you are ready to release the new version of the application to your
production server, all you need to do is grab the updated version of your
application, which will include the new migration script, and run flask db
upgrade. Alembic will detect that the production database is not updated to
the latest revision of the schema, and run all the new migration scripts
that were created after the previous release.

As I mentioned earlier, you also have a flask db downgrade command, which
undoes the last migration. While you will be unlikely to need this option on
a production system, you may find it very useful during development. You may
have generated a migration script and applied it, only to find that the
changes that you made are not exactly what you need. In this case, you can
downgrade the database, delete the migration script, and then generate a new
one to replace it.
'''

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    r'''
    The User class has a new posts field, that is initialized with
    db.relationship. This is not an actual database field, but a high-level view
    of the relationship between users and posts, and for that reason it isn't
    in the database diagram. For a one-to-many relationship, a db.relationship
    field is normally defined on the "one" side, and is used as a convenient way
    to get access to the "many". So for example, if I have a user stored in u,
    the expression u.posts will run a database query that returns all the posts
    written by that user.
    
    The first argument to db.relationship is the model class that represents the
    "many" side of the relationship. This argument can be provided as a string
    with the class name if the model is defined later in the module. The backref
    argument defines the name of a field that will be added to the objects of
    the "many" class that points back at the "one" object. This will add a
    post.author expression that will return the user given a post. The lazy
    argument defines how the database query for the relationship will be issued,
    which is something that I will discuss later. Don't worry if these details
    don't make much sense just yet, I'll show you examples of this at the end of
    this article.
    
    Since I have updates to the application models, a new database migration needs to be generated:

    (venv) (base) PS C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog> flask db migrate -m "posts table"
    Traceback (most recent call last):
    File "C:\Users\rcasu\miniconda3\lib\runpy.py", line 197, in _run_module_as_main
        return _run_code(code, main_globals, None,
    File "C:\Users\rcasu\miniconda3\lib\runpy.py", line 87, in _run_code
        exec(code, run_globals)
    File "C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog\venv\Scripts\flask.exe\__main__.py", line 7, in <module>
    File "C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog\venv\lib\site-packages\flask\cli.py", line 1063, in main
        cli.main()
    File "C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog\venv\lib\site-packages\click\core.py", line 1055, in main
        rv = self.invoke(ctx)
    File "C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog\venv\lib\site-packages\click\core.py", line 1651, in invoke
        cmd_name, cmd, args = self.resolve_command(ctx, args)
    File "C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog\venv\lib\site-packages\click\core.py", line 1698, in resolve_command    
        cmd = self.get_command(ctx, cmd_name)
    File "C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog\venv\lib\site-packages\flask\cli.py", line 578, in get_command
        app = info.load_app()
    File "C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog\venv\lib\site-packages\flask\cli.py", line 308, in load_app
        app = locate_app(import_name, name)
    File "C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog\venv\lib\site-packages\flask\cli.py", line 218, in locate_app
        __import__(module_name)
    File "C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog\microblog.py", line 1, in <module>
        from app import app
    INFO  [alembic.autogenerate.compare] Detected added index 'ix_post_timestamp' on '['timestamp']'
    INFO  [alembic.autogenerate.compare] Detected type change from VARCHAR(length=120) to String(length=128) on 'user.password_hash'
    Generating C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog\migrations\versions\d1506372820f_posts_table.py ...  done
    (venv) (base) PS C:\Users\rcasu\Documents\demos\flask-mega-tutorial\microblog> flask db upgrade
    INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
    INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
    INFO  [alembic.runtime.migration] Running upgrade dd60320d0ec8 -> d1506372820f, posts table
    '''
    
    r'''
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
    
'''
    Database Relationships:
    Relational databases are good at storing relations between data items.
    Consider the case of a user writing a blog post.
    The user will have a record in the users table, and the post will have a
    record in the posts table. The most efficient way to record who wrote a
    given post is to link the two related records.

    Once a link between a user and a post is established, the database can
    answer queries about this link. The most trivial one is when you have a blog
    post and need to know what user wrote it. A more complex query is the
    reverse of this one. If you have a user, you may want to know all the posts
    that this user wrote. Flask-SQLAlchemy will help with both types of queries.
'''

class Post(db.Model):
    '''
    The new Post class will represent blog posts written by users. The timestamp
    field is going to be indexed, which is useful if you want to retrieve posts
    in chronological order. I have also added a default argument, and passed the
    datetime.utcnow function. When you pass a function as a default, SQLAlchemy
    will set the field to the value of calling that function (note that I did
    not include the () after utcnow, so I'm passing the function itself, and not
    the result of calling it). In general, you will want to work with UTC dates
    and times in a server application. This ensures that you are using uniform
    timestamps regardless of where the users are located. These timestamps will
    be converted to the user's local time when they are displayed.
    '''
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    '''
    The user_id field was initialized as a foreign key to user.id, which means
    that it references an id value from the users table
    (<table_name>.<column_name>). In this reference the
    user part is the name of the database table for the model. It is an
    unfortunate inconsistency that in some instances such as in a
    db.relationship() call, the model is referenced by the model class, which
    typically starts with an uppercase character, while in other cases such as
    this db.ForeignKey() declaration, a model is given by its database table
    name, for which SQLAlchemy automatically uses lowercase characters and, for
    multi-word model names, snake case.
    '''

    def __repr__(self):
        return '<Post {}>'.format(self.body)
    
    