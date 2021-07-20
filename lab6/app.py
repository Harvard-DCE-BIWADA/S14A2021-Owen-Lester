from dotenv import load_dotenv
from flask import Flask, flash, render_template, request, url_for, redirect, jsonify, session
from models.models import Db, User, Post
from forms.forms import SignupForm, LoginForm, NewpostForm
from os import environ
from passlib.hash import sha256_crypt
import gunicorn

load_dotenv('.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL').replace('postgres://', 'postgresql://') # this is to solve a bug in heroku
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = environ.get('SECRET_KEY') # Make sure this is set in Heroku dashboard for this new app!
Db.init_app(app)
app.jinja_env.filters['zip'] = zip

# User CRUD
# Create a new user /user/create
@app.route( '/user/create', methods=['POST'])
def user_create():
    # Init credentials from form request
    username = request.form['username']
    password = request.form['password']

    # Init user from Db query
    existing_user = User.query.filter_by(username=username).first()

    # Control new credentials
    if username == '' or existing_user:
        flash('The username already exists. Please pick another one.')
        return redirect(url_for('signup'))
    else:
        user = User(username=username, password=sha256_crypt.hash(password))
        Db.session.add(user)
        Db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
        
# HW: Complete CRUD methods for User class
#       NOTE: Each of the following routes should redirect the user to the login page if the user is not logged in!
# HW: Add /user/retrieve/<uid>
@app.route('/user/retrieve/<uid>')
def retrieve_user(uid):
    if 'username' in session and session['username'] != '' and int(uid) == User.query.filter_by(username=session['username']).first().uid:
        user = User.query.filter_by(uid=uid).first()
        print("HEEEELLLOO")
        return render_template('user_profile.html', user = user)
    else:
        return redirect(f'/login')




# HW: Add /user/update
@app.route('/user/update/<username>/<password>')
def update_user(username, password):
    if 'username' in session and session['username'] != '':
        user = User.query.filter_by(username = session['username']).first()
        user.username = username
        session['username'] = username
        user.password = sha256_crypt.hash(password)
        Db.session.commit()

    return redirect(f'/login')
# HW: Add /user/delete

@app.route('/user/delete')
def delete_user():

    if 'username' in session and session['username'] != '':
        user = User.query.filter_by(username=session['username']).first()
        if  user != None:
            uid = user.uid
            posts = Post.query.filter_by(author = uid).all()
            Db.session.delete(user)
            for post in posts:
                Db.session.delete(post)
            Db.session.commit()
            session.clear()
    return redirect('/login')




# Post CRUD
# /post/create
@app.route('/post/create', methods=['POST'])
def newpost():
    # HW: Redirect user if they are not logged in!
    # Init user from poster
    session_user = User.query.filter_by(username=session['username']).first()

    # Init content from form request
    content = request.form['content']

    # Create in DB
    new_post = Post(author=session_user.uid, content=content)
    Db.session.add(new_post)
    Db.session.commit()

    return redirect(url_for('index'))

# HW: Complete CRUD methods for Post class
#       NOTE: Each of the following routes should redirect the user to the login page if the user is not logged in!      
# HW: Add /post/retrieve/<pid>
@app.route('/user/retrieve/<pid>')
def retrieve_post(pid):
    post = Post.query.filter_by(pid=pid).first()
    return render_template('user_profile.html', user = user)

# HW: Add /post/update
# HW: Add /post/delete

# Default route
@app.route('/')
@app.route('/index')
def index():
    # Control by login status
    print(session)
    if 'username' in session and session['username'] != '':
        session_user = User.query.filter_by(username=session['username']).first()
        posts = Post.query.filter_by(author=session_user.uid).all()
        users = []
        for i in posts:
            users.append(User.query.filter_by(uid=i.author).first().username)
        return render_template('index.html', title='Home', posts=posts, users = users, session_username=session_user.username)
    else:
        all_posts = Post.query.all()
        users = []
        for i in all_posts:
            users.append(User.query.filter_by(uid=i.author).first().username)
        form = NewpostForm()
        return render_template('index.html', title='Home', posts=all_posts,users = users, post_form=form)


#GET & POST /login
@app.route('/login', methods=['GET', 'POST'])
def login():

    # Init form
    form = LoginForm()

    # If post
    if request.method == 'POST':

        # Init credentials from form request
        username = request.form['username']
        password = request.form['password']

        # Init user by Db query
        user = User.query.filter_by(username=username).first()
        print(user)

        # Control login validity
        if user is None or not sha256_crypt.verify(password, user.password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        else:
            session['username'] = username
            return redirect(url_for('index'))

    # If GET
    else:
        return render_template('login.html', title='Login', form=form)


#POST /logout
@app.route('/logout', methods=['POST'])
def logout():
    # Logout
    session.clear()
    return redirect(url_for('index'))

# Register as a new user /signup
@app.route('/signup')
def signup():
    # Init form
    form = SignupForm()

    return render_template( 'signup.html', title='Signup', form=form )

# Load the new post form
@app.route('/new_post')
def new_post():
    # Init form
    form = NewpostForm()
    
    return render_template('new_post.html', title='New Post', form=form )