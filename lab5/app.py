from dotenv import load_dotenv
from os import environ
from flask import Flask, redirect, render_template, jsonify, url_for, request
from models.homeworkuser import HomeworkUser, Db
from forms.forms import Form
from dotenv import load_dotenv
from os import environ
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from models.homeworkuser import HomeworkUser, Db
#import gunicorn

# Load environment
load_dotenv('.env')

# Initialize app
app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY')

# Initialize DB
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL').replace('postgres://', 'postgresql://') # this is to solve a bug in heroku
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Db.init_app(app)


@app.route('/')
def index():

    # Take a look :^)
    users = HomeworkUser.query.all()
    print('# users:', len(users))

    return render_template("index.html")


@app.route('/load_data', methods=['GET'])
def load_data():
    users_json = {'users': []}
    users = HomeworkUser.query.all()
    for user in users:
        user_info = user.__dict__
        del user_info['_sa_instance_state']
        users_json['users'].append(user_info)
    return jsonify(users_json)

@app.route('/list', defaults={ 'offset' : 0, 'limit' : 25 }, methods=['GET'] )
@app.route('/list/<offset>', defaults={ 'offset' : 0, 'limit' : 25 }, methods=['GET'] )
@app.route('/list/<offset>/<limit>/', methods=['GET'] )
def list( offset, limit ):
    offset = int( offset )
    limit = int( limit )
    
    # get the pagination limits
    total = len( HomeworkUser.query.all() ) # count the total number of records
    pages = { 'begin' : 0 };
    pages[ 'prev' ] = max( offset - limit, 0 ) # don't want a negative index!
    pages[ 'current' ] = min( max( 0, offset ), total ) # gotta be in range!
    pages[ 'next' ] = min( offset + limit, total - limit ) # don't want to go over
    pages[ 'end' ] = total - limit # just get the end.
    print( offset, limit, pages )
    
    # get just the users we want to show
    users = HomeworkUser.query.offset( offset ).limit( limit ).all()
    
    return render_template( "list.html", users=users, pages=pages, limit=limit )

#
# RUD - create
#REST API - special API to manipulate object directly
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/#inserting-records
#user API with method create and all of the variables we want to create a new user
#No mehtods: GET because we are allowing both POST and GET - all methods
# E.g.: /user/create/jjessup/Jared/Jessup/javascript/5/34/8
#@app.route('/user/create/<username>')
@app.route('/user/create/<username>/<first_name>/<last_name>/<prog_lang>/<experience_yr>/<age>/<hw1_hrs>')
def create_user(username, first_name, last_name, prog_lang, experience_yr, age, hw1_hrs):
    # Create
    #Need to sanatize the data - make sure the data is in the correct format and is appropriate (like age of being 1000)
    user = HomeworkUser(username=username, first_name=first_name, last_name=last_name, prog_lang=prog_lang, experience_yr=experience_yr, age=age, hw1_hrs=hw1_hrs)
    Db.session.add(user)
    Db.session.commit() #We commit because it will do everything at once - for performance
    print('Created:', user.toString())

    return redirect(f'/user/read/{user.username}') #Tells browser to go to another route
    
    # Question: How else could we implement this?


# CRUD - read
# E.g. /user/read/101
@app.route('/user/read/<username>')
def read_user(username):
    # Read
    user = [ HomeworkUser.query.filter_by( username = username ).first() ]
    print('Read:', user[0].toString())

    return render_template('list.html', users=user) #No pages variable so doesn't run the pages stuff in list.html


# CRUD - update FIXME
# https://stackoverflow.com/questions/6699360/flask-sqlalchemy-update-a-rows-information
# https://docs.sqlalchemy.org/en/13/core/dml.html#sqlalchemy.sql.expression.update
# E.g.: /user/update/jjessup/John Bob/Jessup/javascript/5/34/8
#@app.route('user/update/<username>', method = ['POST'])
@app.route('/user/update/<username>/<first_name>/<last_name>/<prog_lang>/<experience_yr>/<age>/<hw1_hrs>')
def update_user(username, first_name, last_name, prog_lang, experience_yr, age, hw1_hrs):
    # TODO - find this user by uid
    user = HomeworkUser.query.filter_by( username = username ).first()
    # TODO - update the fields for this user
    user.first_name = first_name
    user.last_name = last_name
    user.prog_lang = prog_lang
    user.experience_yr = experience_yr
    user.age = age
    user.hw1_hrs = hw1_hrs

    Db.session.commit()

    return redirect(f'/user/read/{user.username}')


# CRUD - delete FIXME
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/#deleting-records
# E.g. /user/delete/101
@app.route('/user/delete/<username>')
def delete_user(username):
    # TODO - find this user by username
    user = HomeworkUser.query.filter_by(username=username).first()
    
    # TODO - delete this user, return to all users
    # (hint: can we use an api like add(user) to delete one? how do we commit changes to the db? )
    Db.session.delete(user)
    Db.session.commit()
    return redirect( '/list' )#Go to list

@app.route('/form')
def form():

    # Instantiate form
    form = Form()

    return render_template('form.html', form=form)

@app.route('/user/create', methods = ['post'])
def create():
    user = HomeworkUser(username=request.form["username"], first_name=request.form["first_name"], last_name=request.form["last_name"], prog_lang=request.form["prog_lang"],
                        experience_yr=request.form["experience_yr"], age=request.form["age"], hw1_hrs=request.form["hw1_hours"])
    Db.session.add(user)
    Db.session.commit()
    return redirect(f'/user/read/{user.username}')

@app.route('/user/update', methods = ['post'])
def update():
    user = HomeworkUser.query.filter_by(username=request.form["username"]).first()
    if user != None:
        return render_template('update_form.html', user = user)
    else:
        return redirect(f'/form')

@app.route('/form_update')
def update_form():
    return render_template('form_update.html')

@app.route('/updating_user/<username>', methods = ['post'])
def updating_user(username):
    # TODO - find this user by uid
    user = HomeworkUser.query.filter_by( username = username ).first()
    # TODO - update the fields for this user
    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.prog_lang = request.form["prog_lang"]
    user.experience_yr = request.form["experience_yr"]
    user.age = request.form["age"]
    user.hw1_hrs = request.form["hw1_hrs"]
    Db.session.commit()
    return redirect(f'/user/read/{user.username}')


@app.route('/deleting_user')
def deleting_user():
    return render_template('form_delete.html')
@app.route('/d_user',  methods = ['post'])
def d_user():
    user = HomeworkUser.query.filter_by(username=request.form["username"]).first()
    if user != None:
        return redirect(f'/user/delete/{user.username}')
    else:
        return redirect(f'/list')
