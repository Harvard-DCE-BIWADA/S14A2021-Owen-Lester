# Lab 7

Welcome! This week we extend our application to include followers.

## Before you get started

Perform the steps A1-10 listed in the [labs.md](../lab0/labs.md) file as usual.
Perform the same steps as you did in lab 6.
Copy all of your lab6 templates, static variables, models, app.py into the lab7 folder, we are going to reuse all of it.

## References 

1. Keeping in mind, there is more functionality with Flask and databases:
    + Database management with [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/).
    + Database relationships (and more) with (Miguel Grinberg)[https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database].

2. Types of relationships:
    + *One-to-one* - e.g., one post has one user.
    + *One-to-many* - e.g., one user has many posts.
    + *Many-to-many* - e.g., users following users.
        + Apply an association table to break down many-to-many to many-to-one.
        + These relationships are self-referential (of the same class).

## Homework
1. Setup a new lab7 database:
    + Update your .env with new DATABASE_URL: `postgresql://localhost/lab7` (Modify appropriately for windows)
    + Create (psql): `CREATE DATABASE lab7;`.
    + Connect (psql): `\c lab7;`
    + Update (psql): `\i data/lab7.sql;`.
    + **Your turn:** update your 'models.py' to include new tables (make sure to import in app.py).
    
2. Create a strategy for accessing a user's profile (see Extras #1 for more).
    + Add a new route to your app.py similar to the below:
        ```
        # GET /profile/<username>
        @app.route('/profile/<username>', methods=['GET'])
        def profile(username):
        
            # Control by login status
            if 'username' in session:
        
                # Retrieve session user
                
                # Retrieve profile user
        
                # Retrieve posts
        
                # Check to see if follow relationship exists
        
                return render_template('profile.html', user=profile_user, posts=profile_user_posts, followed=followed)
        
            else: 
        
                return redirect(url_for('index'))
        
        ```
    + Add some Html to your profile.html content block:
        ```
        <h1>Profile: {{ user.username }} !</h1>
        
        {% if followed %}
        <form id="following_form" action="/profile/{{ user.username }}/unfollow" method="post">
            <button>Unfollow</button>
        </form>
        {% else %}
        <form id="following_form" action="/profile/{{ user.username }}/follow" method="post">
            <button>Follow</button>
        </form>
        {% endif %}
        ```
3. Add follow / unfollow functionality in the routes:
```
# GET /profile/<username>/follow
@app.route('/profile/<username>/follow', methods=['POST'])
def follow(username):

    # Get session user

    # Retrieve profile user

    # Add Follow entry

    return redirect(url_for('profile', username=username))


# GET /profile/<username>/unfollow
@app.route('/profile/<username>/unfollow', methods=['POST'])
def unfollow(username):

    # Get session user

    # Retrieve profile user

    # Remove entry

    return redirect(url_for('profile', username=username))
```

4. Modify your logic for "likes" from lab6 to add a new relationship to the likes table so that:
    + Users cannot "like" their own posts.
    + Once liked, users cannot like them again but can dislike.

    
## Extras (Required for Grad Students)
1. Create a search component:
    + A small search bar form:
        ```
        <form action='/search' method='POST'>
        <input type='text' name='search_box'></input>
        <button type='submit'> Search </button>
        </form>
        ```
    + A route to handle the results:
    ```
    @app.route('/search', methods=['POST'])
    def search():
        user_to_query = request.form['search_box']
        return redirect(url_for('profile', username=user_to_query))
    ```
   
2. If you are working with joins, try implementing these class methods for the User model:
    ```
    @classmethod
    def is_following(self, user):
        print('Followed', self.followed)
        return self.followed.filter(Follows.c.following == user.uid).count() > 0
    
    @classmethod
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
    
    @classmethod
    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
    ```