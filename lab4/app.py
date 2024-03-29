from dotenv import load_dotenv
from os import environ
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.homeworkuser import HomeworkUser, Db
import gunicorn
# Load environment
load_dotenv('.env')

# Initialize app
app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY')

# Initialize DB
Db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DATABASE_URL").replace("postgres://", "postgresql://")
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
@app.route('/list')
def list():
    users = HomeworkUser.query.all()
    all = []
    pages = []
    for num,user in enumerate(users):
        user_info = user.__dict__
        del user_info['_sa_instance_state']
        pages.append(user_info.values())
        if (num+1)%25 == 0:
            all.append(pages)
            pages = []
    head = user.__dict__.keys()
    return render_template("list.html", user_info=all, head = head)
