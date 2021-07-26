from dotenv import load_dotenv
from flask import Flask, flash, render_template, request, url_for, redirect, jsonify, session
from models.models import Db, User, Post, Follows, Likes
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
        return render_template('profile.html', user = user, purpose = "post")
    else:
        session.clear()
        return redirect(f'/login')




# HW: Add /user/update
@app.route('/update')
def user_update():
    if 'username' in session and session['username'] != '':
        return render_template("user_update.html", user = User.query.filter_by(username = session["username"]).first())
    else:
        return redirect(f'/login')

@app.route('/user/update',  methods = ['post'])
def update_user():
    user = User.query.filter_by(username = session['username']).first()
    user.username = request.form["username"]
    session['username'] = request.form["username"]
    user.password = sha256_crypt.hash(request.form["password"])
    Db.session.commit()
    session.clear()
    return redirect(f'/login')
# HW: Add /user/delete

@app.route('/user/delete')
def delete_user():

    if 'username' in session and session['username'] != '':
        user = User.query.filter_by(username=session['username']).first()
        if  user != None:
            uid = user.uid
            posts = Post.query.filter_by(uid = uid).all()
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
    new_post = Post(uid=session_user.uid, content=content)
    Db.session.add(new_post)
    Db.session.commit()

    return redirect(url_for('index'))

# HW: Complete CRUD methods for Post class
#       NOTE: Each of the following routes should redirect the user to the login page if the user is not logged in!      
# HW: Add /post/retrieve/<pid>
@app.route('/user/retrieve/<pid>')
def retrieve_post(pid):
    post = Post.query.filter_by(pid=pid).first()
    if 'username' in session and session['username'] != '' and post.uid == User.query.filter_by(username= session["username"]).first().uid:
        return render_template('profile.html',  purpose = "post", post = post)
    else:
        session.clear()
        return redirect('/login')


# HW: Add /post/update
@app.route('/update_post')
def post_update():
    session_user = User.query.filter_by(username=session['username']).first()
    posts = Post.query.filter_by(uid=session_user.uid).all()
    return render_template('post_update.html', posts = posts)

@app.route('/post/update',  methods = ['post'])
def update_post():
    user = User.query.filter_by(username = session['username']).first()
    posts = Post.query.filter_by(uid = user.uid).all()
    for post in posts:
        if request.form[f'content{post.pid}'] == '':
            pass
        else:
            post.content = request.form[f'content{post.pid}']
    Db.session.commit()
    return redirect(f'/index')


# HW: Add /post/delete

@app.route('/post/delete/<pid>')
def delete_post(pid):
    if 'username' in session and session['username'] != '':
        user = User.query.filter_by(username=session['username']).first()
        if  user != None:
            post = Post.query.filter_by(pid = pid).first()
            if post != None and post.uid == user.uid:
                Db.session.delete(post)
                Db.session.commit()
    return redirect('/index')

# Default route
@app.route('/')
@app.route('/index')
def index():
    # Control by login status
    print(session)
    print()
    if 'username' in session and session['username'] != '':
        session_user = User.query.filter_by(username=session['username']).first()
        posts = Post.query.filter_by(uid=session_user.uid).all()
        users = []
        for i in posts:
            users.append(User.query.filter_by(uid=i.uid).first().username)
        return render_template('index.html', title='Home', posts=posts, users = users, session_username=session_user.username)
    else:
        all_posts = Post.query.all()
        users = []
        for i in all_posts:
            users.append(User.query.filter_by(uid=i.uid).first().username)
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



@app.route('/profile/<username>', methods=['GET'])
def profile(username):
    # Control by login status
    if 'username' in session:

        # Retrieve session user
        session_user = User.query.filter_by(username=session["username"]).first()

        # Retrieve profile user
        profile_user = User.query.filter_by(username=username).first()
        print(session_user)
        print(username)

        # Retrieve posts
        profile_user_posts = Post.query.filter_by(uid=profile_user.uid).all()

        # Check to see if follow relationship exists
        followed = True

        if Follows.query.filter_by(following = profile_user.uid, follower = session_user.uid).first() is None:
            followed = False



        return render_template('real_profile.html', user=profile_user, posts=profile_user_posts, followed=followed, session_user = session_user)

    else:

        return redirect(url_for('index'))

@app.route('/search', methods = ["POST"])
def search():
    user_to_query = request.form['search_box']
    return redirect(url_for('profile', username = user_to_query))

# GET /profile/<username>/follow
@app.route('/profile/<username>/follow', methods=['POST'])
def follow(username):
    if 'username' in session:
        # Get session user
        session_user = User.query.filter_by(username=session["username"]).first()


        # Retrieve profile user
        profile_user = User.query.filter_by(username=username).first()
        username = profile_user.username

        # Add Follow entry
        follower = Follows(following = profile_user.uid, follower = session_user.uid )
        Db.session.add(follower)
        Db.session.commit()

    return redirect(url_for('profile', username=username, session_user = session_user))


# GET /profile/<username>/unfollow
@app.route('/profile/<username>/unfollow', methods=['POST'])
def unfollow(username):
    if 'username' in session:

        # Get session user
        session_user = User.query.filter_by(username=session["username"]).first()

        # Retrieve profile user
        profile_user = User.query.filter_by(username=username).first()
        username = profile_user.username

        # Remove entry
        follower = Follows.query.filter_by(following = profile_user.uid, follower = session_user.uid).first()

        Db.session.delete(follower)
        Db.session.commit()

    return redirect(url_for('profile', username=username, session_user = session_user))

@app.route('/like/<pid>', methods = ["POST"])
def like(pid):
    if 'username' in session:
        session_user = User.query.filter_by(username=session["username"]).first()
        if Likes.query.filter_by(uid=session_user.uid, pid = pid).first() is None:
            if Post.query.filter_by(pid = pid).first().author.uid != session_user.uid:
                lik = Likes(uid = session_user.uid, pid = pid)
                Db.session.add(lik)
                Db.session.commit()
    username = Post.query.filter_by(pid = pid).first().author.username
    return redirect(url_for('profile', username=username, session_user = session_user))

@app.route('/unlike/<pid>', methods = ["POST"])
def unlike(pid):
    if 'username' in session:
        session_user = User.query.filter_by(username=session["username"]).first()
        if Likes.query.filter_by(uid=session_user.uid, pid = pid).first() is not None:
            lik = Likes.query.filter_by(uid=session_user.uid, pid = pid).first()
            Db.session.delete(lik)
            Db.session.commit()
    username = Post.query.filter_by(pid=pid).first().author.username
    return redirect(url_for('profile', username=username, session_user = session_user))