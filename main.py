# -*- coding: utf-8 -*-

from flask import Flask, render_template, g
from sqlite3 import dbapi2 as sqlite3
from settings.dev import DEBUG, DATABASE


app = Flask(__name__)


def connect_db():
    """ Connects to database. """
    rv = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES)
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """ Create database tables. """
    with app.app_context():
        db = get_db()
        with app.open_resource('sql/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db():
    """
       Gets a new database conn for
       current app context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def query_db(query, args=(), fetch_one=False):
    """
        Query DB. 
        To fetch one record include param
        fetch_one = True
    """
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if fetch_one else rv


@app.before_request
def before_request():
    """Get db conn before request"""
    g.db = connect_db()
    

@app.teardown_appcontext
def close_db(error):
    """ Close db again at end of request. """
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', css='index', title='Welcome')
    
    
@app.route("/dashboard", methods=['GET'])
def dashboard():
    return render_template('dashboard.html', css='dashboard', title='Dashboard')


if __name__ == "__main__":
    init_db()
    app.run(debug=DEBUG)
