# Lab 4

Welcome! This week we will be connecting to a Postgres database using models AND we will be introducing data visualization with d3.js.

## Before you get started

Perform the steps A1-10 listed in the [labs.md](../lab0/labs.md) file.

## Installing and Loading the DB

[PostgreSQL](https://www.postgresql.org/) should already be installed for everyone who went through [lab 0](../lab0/readme.md). If not, install it now.

1. Activate Postgres:
    + Macos/Linux/WSL using [Homebrew](https://brew.sh): 
        + `brew services start postgresql`
    + Windows Users:
        1. Open the run popup (windows + R).
        2. Type `services.msc` to open the services panel.
        3. Select the Postgres service and click **Start**.
    + Otherwise:
        + In the terminal type: `psql postgres` (or for some systems just `psql` or `postgres`).
    
    + PSQl commands:
        + List all databases: `\l`
        + List all schemas: `\dn`
        + List all tables: `\dt`
        + List all users: `\du`
        + Connect: `\c`
        + Quit: `\q`
        
    + **NOTE**: For those of you who are knowledgeable about SQL, Postgres _requires_ keywords to be capitalized, and requires semicolons at the end of statements: 
        + `SELECT a FROM b WHERE a > 1;`

2. Install [Psycopg2](https://www.psycopg.org/docs/): `pip install psycopg2`
    + If error, add to PATH (or equivalent for configuration): `export PATH="/Library/PostgreSQL/12/bin/:$PATH"`
    + If another error, `pip install psycopg2-binary`
        
3. Install the other packages needed for this lab:
    + `pip install python-dotenv`
    + `pip install flask-sqlalchemy`
    
4.  Setup the DB
        + Open psql in terminal: `psql postgres`
            + psql: `CREATE DATABASE homework_users_db;`
            + psql: `\c homework_users_db;`
            + FYI - to drop: `DROP DATABASE homework_users_db;`
        + Seed from 'predefined_users.csv'
            + First take a look at './data/seed_db.py' and update user if not 'postgres'.
            + Make sure to update line. 7 with your username!
            + Run: `python data/seed_db.py`.
            + Confirm in psql: `SELECT * FROM homework_users;`.
            
5. Create your environment file (make sure you've installed first with `pip install python-dotenv`):
    + `touch .env`
    + In the new `.env` file, create a variable `SECRET_KEY` and set it to a string of your choice.
        + Note: You will need to set this in heroku later.
    + Import and setup in 'app.py':
        ```
        from dotenv import load_dotenv
        from os import environ
        from flask import Flask, render_template, jsonify
        
        # Load environment
        load_dotenv('.env')
        
        # Initialize app
        app = Flask(__name__)
        app.secret_key = environ.get('SECRET_KEY')
        
        @app.route('/')
        def index():
            return render_template("index.html")
        ```
    + Working into [Heroku](https://devcenter.heroku.com/articles/config-vars).
    + The file itself should be ignored by git, so you will need to create your own. (Question: Why?)
      
6. Build a model for your homework users
    + Create a directory `models` and add a new file `homeworkuser.py`.
    + Import [Flask SqlAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/): `pip install flask-sqlalchemy`
    + Add import, initialize and define class properties:
        ```
        from flask_sqlalchemy import SQLAlchemy

        # Initialize Db
        Db = SQLAlchemy()
        
        class HomeworkUser( Db.Model ):
        
            # Ref. to table
            __tablename__ = 'homework_users'
        
            # Class fields match columns
            uid = Db.Column( Db.Integer, primary_key=True, autoincrement=True )
            username = Db.Column( Db.String(64), nullable=False )
            first_name = Db.Column( Db.String(64), nullable=False )
            last_name = Db.Column( Db.String(64), nullable=False )
            prog_lang = Db.Column( Db.String(64), nullable=False )
            experience_yr = Db.Column( Db.Float, nullable=False )
            age = Db.Column( Db.Integer, nullable=False )
            hw1_hrs = Db.Column( Db.Float, nullable=False )
        ```

7. Connect the database with your Flask app.
    + In `app.py` add/update import statements for your user model:
        ```
        from flask_sqlalchemy import SQLAlchemy
        from models.homeworkuser import HomeworkUser, Db
        ```
    + Also after you initialize your app, configure and connect the db: 
        ```
        # Initialize DB
        Db = SQLAlchemy()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/homework_users_db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        Db.init_app(app)
        ```

5. Add some logic to the `/index` route to confirm a successful connection:
    ```
    # Take a look :^)
        users = HomeworkUser.query.all()
        print('# users:', len(users))
    ```
    
6. Create and populate the template directories needed to display your work.
    + Create a `static` directory, along with `css` and `js` directories underneath. `mkdirs static static/js static/css`
    + Create a template directory, and create or copy a `layout.html` and an `index.html` file within.
    + In the `index.html` template, add the following code inside the `{% block content %}` and `{% endblock %}` tags:
        ```
        <header>
            <h1>D3 from the DB</h1>
            <h2 id="users">Users: </h2>
        </header>
        <div class="slide">
            <div id="vis1" class="vis"></div>
            <!--div id="vis2" class="vis"></div>
            <div id="vis3" class="vis"></div-->
        </div>
        ```

7. Using `.env`
    + On a new line in your `.env` file, copy the url of your database, and set your `DATABASE_URL` variable:
        + Macos/Linux: `DATABASE_URL=postgresql://localhost/homework_users_db`
        + Windows: `DATABASE_URL=postgresql://postgres:<PASSWORD>@localhost/homework_users_db`, replacing <PASSWORD> with your postgresql password.
    + In your `app.py` file, replace the line that says:  
        `app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/homework_users_db'`  
        with:  
        `app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DATABASE_URL").replace("postgres://", "postgresql://")`
    + Test your app's functionality using `flask run` and looking at the logs, which should print out `# users: 100`

## Data Visualization

1. Before moving to the front-side of our application, let's include a method that client call in order to retrieve data from the database:
    ```
    @app.route('/load_data', methods=['GET'])
    def load_data():
        users_json = {'users': []}
        users = HomeworkUser.query.all()
        for user in users:
            user_info = user.__dict__
            del user_info['_sa_instance_state']
            users_json['users'].append(user_info)
        return jsonify(users_json)
    ```

2. [D3.js](https://github.com/d3/d3/blob/master/API.md)
    + Add d3 import reference into `index.html` scripts block: `<script type="text/javascript" src="https://d3js.org/d3.v7.min.js"></script>`.
    + Add a new `main.js` to `static/js/` directory and add this script to `index.html` template: `<script defer type="module" src="{{ url_for('static', filename='js/main.js') }}"></script>`.
    + Create two additional files in your `static/js/` directory:
        + `base.js`
        + `bar.js`
        
    + In `base.js` copy/paste the following code:
        ```
        export class Base {
            constructor( _target, _data ) {}
            
            init() {}
            
            wrangle() {}
            
            render() {}
        }
        export default Base;
        ```

    + In `bar.js` copy/paste the following code:
        ```
        import Base from './base.js'
        
        export class Bar extends Base {
            constructor( _target, _data ) {
                super( _target, _data )
            }
            
            init() {}
            
            wrangle() {}
            
            render() {}
        }
        export default Bar;
        ```
        
    + in `main.js` copy/paste the following code:
        ```
        import { Bar } from './bar.js';
        
        (function(){
            console.log( 'hello world!' )
            d3.json( '/load_data' )
                .then( data => main( data ) )
                .catch( err => console.error( err ) );
        })();
        
        // Global Variables
        function main( data ) {
            // Input to main
            d3.select( "#users" )
                .append( "span" )
                .text( data.users.length )
        
            let	bars = new Bar( data, 'vis1' );
        }
        ```

## Testing & Deployment

1. In your `app.py` file, add the following line with your other imports:
    + `import gunicorn`

2. We need to test our app in heroku! Uh-oh, how do we do that?
    + Read the manual! https://devcenter.heroku.com/articles/heroku-postgresql#using-the-cli
    + Add a postgres database to your heroku app: `heroku addons:create heroku-postgresql:hobby-dev`
    + You will get a database name which will look something like *postgresql-concave-52656*.
    + Push your local database to heroku: `heroku pg:push <DATABASE_URL> <HEROKU_DATABASE_NAME>` 
        + **IMPORTANT!!** replace *DATABASE_URL* with the url you copied into your .env file
        + **IMPORTANT!!** replace *HEROKU_DATABASE_NAME* with the string you got after adding postgres to your heroku app in the previous step.
    + If you make changes to your local database after this point, you'll need to:
        + `heroku pg:reset` and follow the prompts.
        + Push your database again using the command above.
        
    If you ever forget the *HEROKU_DATABASE_NAME*, you can get it back by typing `heroku pg:info` which will list the db name for you.
    
3. Login to your [heroku dashboard](https://dashboard.heroku.com/apps)
    + Navigate to the app for lab4.
    + Click **Settings**.
    + Click the **Reveal Config Vars** button.
    + Add a new config var by typing `SECRET_KEY` in the *KEY* field, and the corresponding value from your `.env` file in the *VALUE* field, and click the **ADD** button.

4. Follow steps B4-11 from [labs.md](../lab0/labs.md)

## Homework

1. Add Bootstrap to your template code as you did in earlier assignments, containing  `<header>`, `<footer>`, and `<main>` tags in the appropriate templates.
    + **REMOVE ANY UNUSED ITEMS FROM THE NAVIGATION THAT ARE NOT USED, AND ADD ANY YOU WILL NEED.**
    + **Use _meaningful_ names for the navigation please.**
2. Modify the `index.html` template so the contents are within bootstrap's container. 
3. Create a new route in your `app.py` called `'/list'` which will list all of the homework users in the database.
4. Create a template which extends `layout.html` and displays all of the data from the `homework_users` table.
5. Fix the 404 error due to a missing favicon. Can you do this without adding any new files? (hint: data url)
6. **EXTRA** (Required for Grad Students): 
    + Modify your `/list` route and template to paginate the data (eg, only showing 25 records at once) and navigation to allow you to move forward and backward through the list. (Bootstrap has some nifty features that make this work. Read the [documentation](https://getbootstrap.com/docs/4.0/components/pagination/)).
