from app import db,app
from flask_login import UserMixin

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.Text)
    desc=db.Column(db.Text)
    poster_id=db.Column(db.Integer,db.ForeignKey('user.id'))

    def __init__(self,title,desc,poster_id):
        self.title = title
        self.desc = desc
        self.poster_id = poster_id

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(10),nullable=False)
    email=db.Column(db.String(30),nullable=False)
    password=db.Column(db.String(128), nullable=False)
    bio=db.Column(db.String(255))
    image_file = db.Column(db.String(20),nullable=True,default="profile_pics/default.jpg")
    posts=db.relationship('Post',backref='poster')

    def __init__(self,username,email,password,bio,image_file):
        self.username =username
        self.email = email
        self.image_file=image_file
        self.password=password
        self.bio=bio

class Comment(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    post_id=db.Column(db.Integer)
    comment=db.Column(db.String(50),nullable=False)
    comment_author=db.Column(db.String(30))

    def __init__(self,comment,comment_author,post_id):
        self.comment = comment
        self.comment_author = comment_author
        self.post_id=post_id
    
with app.app_context():
    db.create_all()