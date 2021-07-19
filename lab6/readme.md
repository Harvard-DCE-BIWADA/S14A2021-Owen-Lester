# Lab 6

Welcome! This week we will be working with user logins and sessions.

## Before you get started

Perform the steps A1-10 listed in the [labs.md](../lab0/labs.md) file as usual.

1. In your `.env` file for lab6, set a SECRET_KEY variable to any string you'd like:
    + `SECRET_KEY=<YOUR_SECRET_KEY>` 
    + Replace `<YOUR_SECRET_KEY>` with your desired key. # Question: How do you include spaces here?

2. Set the same config variable in heroku, by **either**:
    + In the terminal containing your active environment, type: `heroku config:set SECRET_KEY=<YOUR_SECRET_KEY>`, as above.
    + **OR** In your [heroku dashboard](https://dashboard.heroku.com):  
        1. Select your current app.
        2. Click **Settings**.
        3. Click the **Show Config Vars** button.
        4. In the **`KEY`** field, type `SECRET_KEY`.
        5. In the **`VALUE`** field, type your secret key from above.
        6. Press the **+** or **Add** button.
        
3. Confirm the config variable was set by typing `heroku config:get SECRET_KEY` in the terminal containing your active environment.
        
## Prepare your environment

1. In the terminal containing your active environment, change to the lab6 directory and type the following to install all packages needed for this lab:
    + `pipreqs --force .` # this regenerates your requirements.txt file dynamically from the python files in this directory.
    + `pip install -r requirements.txt` # this installs all of the packages listed in the requirements file.
    + If you're still having difficulty, you can install the package manually:
        + The only new library is [passlib](https://passlib.readthedocs.io/en/stable/): `pip install passlib`.
        
## Set up your database

1. Connect to your postgres database installation:
    + Windows: Use the psql shell in C:\Program Files\PostgreSQL13\
    + Mac, Linux, WSL: `psql postgres`
    + **IF YOU CAN'T CONNECT TO THE INSTANCE TELL A TF!!**

2. Create a new database (paying attention to the foreign key):
    + psql: `CREATE DATABASE lab6;`
    + psql: `\c lab6`
    + psql: `CREATE TABLE users(uid SERIAL NOT NULL PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL);`
    + psql: `CREATE TABLE posts(pid SERIAL NOT NULL PRIMARY KEY, author SERIAL NOT NULL, content TEXT NOT NULL, FOREIGN KEY (author) REFERENCES users(uid));`
    + psql: `INSERT INTO users (username, password) VALUES ('Michelle', 'test_pw1');`
    + psql: `INSERT INTO users (username, password) VALUES ('Jasmine', 'test_pw2');`
    + psql: `INSERT INTO posts (author, content) VALUES (1, 'test_post_1');`
    + psql: `INSERT INTO posts (author, content) VALUES (2, 'test_post_2');`
    
    OR
    
    + psql: `CREATE DATABASE lab6;`
    + psql: `\c lab6`
    + psql: `\i data/lab6.sql`
    
3. Confirm that you have created the db successfully:
    + psql: `SELECT * from users;` # This should show 2 rows
    + psql: `SELECT * from posts;` # This should show 2 rows
    
4. Set your `DATABASE_URL` in your `.env` file.
   
## Lab time!

Everything else we have setup for you in the directory :^). We will walk you through how this code works out in the lab.
    + Learn more about [Flask sessions](https://flask.palletsprojects.com/en/1.1.x/api/#flask.session).

## Testing & Deployment

1. Test your code using `flask run`
2. Provision and Publish your database to heroku using the _appropriate_ `heroku pg:push` commands.:
    + Provision a database: `heroku addons:create heroku-postgresql:hobby-dev` 
    + Push your local db to heroku `heroku pg:push <LOCAL_DB_URL> <HEROKU_DB_NAME>`
    + See the last lab and the [Heroku Postgres Documentation](https://devcenter.heroku.com/articles/heroku-postgresql) for more details.
3. Follow steps B7-11 from [lab0/labs.md](../lab0/labs.md).

## Homework

1. Modify all forms, buttons and styles to use Bootstrap!
2. Implement [Message Flashing](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/). Use [Bootstrap Alerts](https://getbootstrap.com/docs/4.0/components/alerts/) to display them, and ensure you include this in the _optimal_ template. (Which one? hint: reuse as much code as possible).
3. Modify the `layout.html` template's navigation to show appropriate navigation items depending on whether the user is signed in or not. 
4. Replace 'Author number' with a user's username.
5. Complete all CRUD methods for Users and Posts. **ENSURE ONLY LOGGED IN USERS CAN EDIT/SEE THEIR _OWN_ PROFILES AND POSTS**.
6. _(Optional)_ Implement [dates](https://docs.sqlalchemy.org/en/13/core/type_basics.html) in your models. **This will require modification of the database.**
7. **EXTRA** _(Required for Grad Students)_:
    + Modify the DB to add a 'likes' field that takes an integer value.
    + Add two routes: `/like/<pid>` and `/dislike/<pid>` which increment or decrement the number of likes, **MAKE SURE ONLY LOGGED IN USERS CAN DO THIS**.
    + Modify the table which displays the posts to add Like/Dislike buttons. Instead of text, use [emojis](https://www.w3schools.com/charsets/ref_emoji.asp) for the links. **DO NOT USE IMAGES**
    + Update your db to fix the passwords for Michelle and Jasmine, so they are properly encoded. (Use your `psql#` prompt to `UPDATE` the records using SQL. See this [example](https://pgpedia.info/s/sha256.html) )

**REMEMBER**: If you make structural changes to your local db, you need to use the `heroku pg:reset` and `heroku pg:push` commands to publish those changes to heroku!
    + See the [Heroku Postgres Documentation](https://devcenter.heroku.com/articles/heroku-postgresql)