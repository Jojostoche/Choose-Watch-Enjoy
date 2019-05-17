from app import app
from flask import g, render_template, redirect, url_for, request, session
from app.db import db_handler
from app.utils import hash_sha1

APP_NAME = "Choose-Watch-Enjoy"

def get_db():
    if 'db' not in g:
        g.db = db_handler()
    return g.db

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/')
@app.route('/index')
def index():
    title= APP_NAME + " | Welcome!"
    return render_template('index.html', title=title)

@app.route('/users')
def users():
    title= APP_NAME + " | List users"
    if session['username']:
        db = get_db()
        users = db.query("SELECT * from user")
        return render_template('users.html', title=title, users=users)
    else:
        return redirect(url_for('login'))

@app.route('/adduser', methods=['POST', 'GET'])
def add_user():
    title= APP_NAME + " | Add a new user"
    error = None
    msg = None
    if session['username']:
        if request.method=='POST':
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            username = request.form['username']
            passwd = request.form['password']
            role = request.form['role']
            if firstname is None or lastname is None or email is None or username is None or passwd is None or role is None:
                error = 'All fields are mandatory.'
            else:
                passwd_hash = hash_sha1(passwd) 
                db = get_db()
                db.add_user(username, passwd_hash, firstname, lastname, email, role)
                msg = 'User was successfully added!'
        return render_template('adduser.html', title=title, msg=msg, error=error)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    title= APP_NAME + " | Login"
    error = None
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hash_sha1(password) 
        db = get_db()
	# custom query
        stored_password = db.get_user_password(username)
        if stored_password != hashed_password:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['username'] = username
            return redirect(url_for('index'))
    return render_template('login.html', title=title, error=error)

@app.route('/logout')
def logout():
    title= APP_NAME + " | Logout"
    g.username = None
    session['username'] = None
    return render_template('logout.html', title=title)

@app.route('/ex1')
def ex1():
    title = "My App - Example 1"
    user = {'username': 'Test'}
    posts = [
        {
            'author': {'username': 'Rambo'},
            'body': 'Beautiful day in Geneva!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('ex1.html', title=title, user=user, posts=posts)

@app.route('/addfilm', methods=['POST', 'GET'])
def add_film():
    title= APP_NAME + " | Add a new film"
    error = None
    msg = None
    if session['username']:
        if request.method=='POST':
        	   original_title = request.form['original_title']
        	   original_language = request.form['original_language']
        	   duration = request.form['duration']
        	   date = request.form['date']
        	   grade = request.form['grade']
        	   age = request.form['age']
        	   if original_title is None or original_language is None or duration is None or date is None or grade is None or age is None :
        	   	error = 'All fields are mandatory.'
        	   else:
        	   	db = get_db()
        	   	db.add_film(original_title, original_language, duration, date, grade, age)
        	   	msg = 'Film was successfully added!'
        return render_template('addfilm.html', title=title, msg=msg, error=error)
    else:
        return redirect(url_for('login'))

@app.route('/films')
def films():
    title= APP_NAME + " | List films"
    db = get_db()
    films = db.query("SELECT * from film")
    return render_template('films.html', title=title, films=films)
    
@app.route('/addactor', methods=['POST', 'GET'])
def add_actor():
    title= APP_NAME + " | Add a new actor"
    error = None
    msg = None
    if session['username']:
        if request.method=='POST':
        	   name = request.form['name']
        	   if name is None :
        	   	error = 'All fields are mandatory.'
        	   else:
        	   	db = get_db()
        	   	db.add_actor(name)
        	   	msg = 'Actor was successfully added!'
        return render_template('addactor.html', title=title, msg=msg, error=error)
    else:
        return redirect(url_for('login'))
        
@app.route('/actors')
def actors():
    title= APP_NAME + " | List actors"
    db = get_db()
    actors = db.query("SELECT * from actor")
    return render_template('actors.html', title=title, actors=actors)
    
@app.route('/addstudio', methods=['POST', 'GET'])
def add_studio():
    title= APP_NAME + " | Add a new studio"
    error = None
    msg = None
    if session['username']:
        if request.method=='POST':
        	   name = request.form['name']
		   zip_code = request.form['zip_code']
		   country = request.form['country']
		   website = request.form['website']
        	   if name is None or if zip_code is None or if country is None or if website is None :
        	   	error = 'All fields are mandatory.'
        	   else:
        	   	db = get_db()
        	   	db.add_studio(name)
        	   	msg = 'Studio was successfully added!'
        return render_template('addstudio.html', title=title, msg=msg, error=error)
    else:
        return redirect(url_for('login'))

@app.route('/studios')
def studios():
    title= APP_NAME + " | List studios"
    db = get_db()
    studios = db.query("SELECT * from studio")
    return render_template('studios.html', title=title, studios=studios)

@app.route('/deletefilm')
def delete_film(request):
    db = get_db()
    db.query("DELETE FROM film WHERE id=" + request.query_string['id']) 
    return redirect(url_for('films'))
