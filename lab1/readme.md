## Lab 1

Welcome! In this lab we will be setting up a Conda environment, a Flask app, and Heroku deployment link.
     
1. Use the terminal to create directories and files, starting at the root of your project:
    + New file e.g. `touch app.py`
    
2. Create a new virtual [environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
    + `conda create --name labenv python=3.8`
    + We can reuse this environment in future labs.
    
5. Activate new virtual environment:
    + With conda: `conda activate labenv`
    
6. Use [PyPI](https://pypi.org/), aka "pip", to install packages:
    + Starting with Flask: `pip install Flask`
    
7. Build your Flask app using the docs:
    + Make use of the guided [quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/).
    + Use the [docs](https://flask.palletsprojects.com/en/1.1.x/) to build efficiently / effectively.
    + The basic app:
        ```
        from flask import Flask
        app = Flask(__name__)
      
        @app.route('/')
        def hello_world():
            return 'Hello, World!'
        ```
    + Run locally (Windows users may replace 'export' with 'set':
        + Configure Flask environment
            + Install `python-dotenv`
            + Create '.flaskenv':
                ```
                FLASK_APP=app.py
                FLASK_RUN_PORT=5005
                FLASK_ENV=development
                ```
        + Run Flask: `flask run`
    + Experiment by creating a new method that allows you to extract variables from a url:
        ```
        @app.route('/<you>')
        def hello_you(you):
            return f'Hello, {you}!'
        ```
      
8. Now build out an application using a 'static' folder and jinga2 templating language:
    + Build a standard framework:
        ```
        /static
            /assets
            /css
                index.css
            /js
        /templates
            index.html
        ```
    + For index.html:
        ```
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Lab 1</title>
        
            <!-- Styles -->
            <link href="{{ url_for('static', filename='./css/index.css') }}" rel="stylesheet">
        </head>
        <body>
        <h1>Hello, {{ bCE }}!</h1>
        </body>
        </html>
        ```
    + For index.css:
        ``` 
        h1 {
            color: rgba(0, 0, 64, 1);
        }
        ```
    + For app.py
        ```
        from flask import Flask, render_template
      
        app = Flask(__name__)


        @app.route('/')
        def index():
            bestClassEver = 'Best Class Ever'
            return render_template('index.html', bCE=bestClassEver)
        
        
        @app.route('/world')
        def hello_world():
            return 'Hello, World!'
        
        
        @app.route('/<you>')
        def hello_you(you):
            return f'Hello, {you}!'
        ```
    + Check the browser!
    
9. Create a package requirements and setup for deployment using gunicorn:
    + Install gunicorn: `pip install gunicorn`
    + To save your pip installs: `pip freeze > requirements.txt`
    + Create a 'Procfile' and include: `web: gunicorn app:app`
    
10. Get on Git:
    + Create a .gitignore, and add (at least):
        ```
        .sublime-workspace
        .idea
        .DS_store
        ```
    + Check status: `git status`
    + Add all files: `git add .`
    + Commit with message: `git commit -m "Init commit"`
    + Push upstream to master branch: `git push -u origin master`
    
11. Setup for deployment to Heroku:
    + Setup a free account at [Heroku](https://signup.heroku.com/login).
    + Please follow this [guide](https://devcenter.heroku.com/articles/heroku-cli) to setup Heroku's CLI (command
     line interface).
    + Use the command line to login to Heroku in the browser (you may need to create a new account): `heroku login`
    + Create a new heroku app: `heroku create --buildpack heroku/python`
    + Check to see if you have a heroku repo listed `git remote -v`
    + If not, add one using `git remote add heroku <<HEROKU GIT URL GOES HERE>>`
    + Push git repo to heroku: `git push heroku master`
    + If (when) you receive an error, look carefully at the errors!
    + You will need to copy your requirements.txt file for this app up one level: `cp requirements.txt ../requirements.txt`
    + Add that file, commit and push before pushing to heroku again!

12. Celebrate your first app in the browser - a whole new world!

13. HW: Add to your experience using templates with [jinja2](https://jinja.palletsprojects.com/en/2.11.x/templates/):
    + Move generic layout into `layout.html`
    + Create a small `header.html` to include in your layout.
    + Create `index.html` as an extension.
    + Try to use a Google font and add a little style to your work.

14. EXTRA: Install and use the `pipreqs` command to generate your requirements document dynamically:  
     + [readme-pipreqs.md](./resources/readme-pipreqs.md) for notes.
     + Google 'pipreqs' for more info.

