# -*- coding: utf-8 -*-

from flask import Flask, render_template, g, request, url_for, redirect,\
                  session, abort
from sqlite3 import dbapi2 as sqlite3
from settings.dev import DEBUG, DATABASE, SECRET_KEY, USERNAME, PASSWORD
from models.user_model import User
from utils.db import CREATE_USER


app = Flask(__name__)
app.secret_key = SECRET_KEY


#DATABASE CODE

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
        
        
#END OF DATABASE CODE        
        
        
#ROUTES/HANDLERS

##Admin
@app.route("/admin", methods=['GET'])
def admin_index():
    if session:
        if session['logged_in']:
            if session['admin']:
                return redirect(url_for('admin_dashboard'))
    else:
        return render_template('admin_index.html', title='Admin Index/Login')


@app.route("/admin/login", methods=['POST'])
def admin_login():
    if request.form['username'] == USERNAME:
        if request.form['password'] == PASSWORD:
            session['logged_in'] = True
            session['admin'] = True
            return redirect(url_for('admin_dashboard'))
    else: 
        return redirect(url_for('admin_index'))
        
        
@app.route('/admin/logout')
def admin_logout():
    session.pop('logged_in', None)
    session.pop('admin', None)
    return redirect(url_for('admin_index'))
        

@app.route("/admin/dashboard", methods=['GET'])
def admin_dashboard():
    if not session.get('logged_in'):
            abort(401)
    if not session.get('admin'):
            abort(401)
    return render_template('admin_dashboard.html')
    

@app.route('/admin/user/create', methods=['POST'])
def admin_create_user():
    if not session.get('logged_in'):
            abort(401)
    if not session.get('admin'):
            abort(401)
    
    user = User(request.form['name'],
                request.form['phone'],
                request.form['email'],
                request.form['organization']
                )
                
                
    query_db(CREATE_USER, [user.name, 
                           user.phone, 
                           user.email, 
                           user.organization, 
                           user.status, 
                           user.role])
    
    #flash the message tat user was created
    #redirect to dashboard main.                       
    return 'user created successfully.'
   
    
    
    
##END OF ADMIN 


@app.route("/dashboard", methods=['GET'])
def dashboard():
    return render_template('dashboard.html', css='dashboard', title='Dashboard')
   

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', css='index', title='Welcome')
     

@app.route("/new/client", methods=['GET'])
def new_client():
    return render_template('new_client.html', title='Add New Client')
    
    
@app.route("/new/list", methods=['GET'])
def new_list():
    return render_template('new_list.html', title='Create New Call List')
    
    
@app.route("/new/script", methods=['GET'])
def new_script():
    return render_template('new_script.html', title='Create New Call Script')


if __name__ == "__main__":
    init_db()
    app.run(debug=DEBUG)
