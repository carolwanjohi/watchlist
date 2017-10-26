from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    '''
    @login_manager.user_loader Passes in a user_id to this function
    Function queries the database and gets a user's id as a response
    '''
    return User.query.get(int(user_id))

class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count

class Review(db.Model):
    '''
    Review class to define a movie review in the database
    '''

    # Name of the rable
    __tablename__ = 'reviews'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key=True)

    # movie_id column for a movie's id
    movie_id = db.Column(db.Integer)

    # movie_title column for a movie's title
    movie_title = db.Column(db.String)

    # image_path column for a movie's poster
    image_path = db.Column(db.String)

    # movie_review column for a movie's review
    movie_review = db.Column(db.String)

    # posted column for a review's date 
    posted = db.Column(db.Time, default=datetime.utcnow())

    # user_id column for linking a review to a specific user
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_review(self):
        '''
        Save instance of Review model to the session and commit it to the database
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls,id):
        '''
        Function to retrive reveiws for a specific movie

        Args:
            id : movie id
        '''
        reviews = Review.query.filter_by(movie_id=id).all()
        return reviews

class User(UserMixin,db.Model):
    '''
    User class to define a user in the database
    '''

    # Name of the table
    __tablename__ = 'users'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # username column for usernames
    username = db.Column(db.String(255))

    # email column for a user's email address
    email = db.Column(db.String(255), unique=True, index=True)

    # role_id column for a User's role
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    # bio column for a user's biography
    bio = db.Column(db.String(255))

    # profile_pic_path column for a user's profile picture
    profile_pic_path = db.Column(db.String())

    # password_hash column for passwords
    password_hash = db.Column(db.String(255))

    # virtual column to connect with foriegn key
    reviews = db.relationship('Review', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    '''
    Role class to define a User's role in the database
    '''

    # Name od the table
    __tablename__ = 'roles'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # name column for the name of the roles
    name = db.Column(db.String(255))

    # virtual column to connect with foriegn key
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'










