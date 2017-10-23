from . import db
from werkzeug.security import generate_password_hash,check_password_hash

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

class Review:
    '''
    Review class to define a movie review
    '''

    # Empty reviews list
    all_reviews = []

    def __init__(self, movie_id, title, imageurl, review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):
        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response


class User(db.Model):

    # Name of the table
    __tablename__ = 'users'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # username column for usernames
    username = db.Column(db.String(255))

    # role_id column for a User's role
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    # pass_secure column for passwords
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):

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










