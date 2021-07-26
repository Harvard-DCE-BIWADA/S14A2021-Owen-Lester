from flask_sqlalchemy import SQLAlchemy

Db = SQLAlchemy()


class User(Db.Model):
    __tablename__ = 'users'
    uid = Db.Column(Db.Integer, primary_key=True, autoincrement=True)
    username = Db.Column(Db.String(64), unique=True, nullable=False)
    password = Db.Column(Db.String(128), nullable=False)



class Post(Db.Model):
    __tablename__ = 'posts'
    pid = Db.Column(Db.Integer, primary_key=True, autoincrement=True)
    uid = Db.Column(Db.Integer, Db.ForeignKey('users.uid'), nullable=False)
    content = Db.Column(Db.String(1024), nullable=False)
    author = Db.relationship("User", backref ='post')

class Follows(Db.Model):
    __tablename__ = 'follows'
    fid = Db.Column(Db.Integer, primary_key = True, autoincrement = True)
    follower = Db.Column(Db.Integer, Db.ForeignKey('users.uid'), nullable = False)
    following = Db.Column(Db.Integer, Db.ForeignKey('users.uid'), nullable = False)

class Likes(Db.Model):
    __tablename__ = "likes"
    uid = Db.Column(Db.Integer, Db.ForeignKey('users.uid'), nullable=False, primary_key = True)
    pid = Db.Column(Db.Integer, Db.ForeignKey('posts.pid'), nullable=False, primary_key = True)
