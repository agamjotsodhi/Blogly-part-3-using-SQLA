"""Models for Blogly."""
"""SQLAlchemy models for blogly."""


import datetime
from flask_sqlalchemy import SQLAlchemy


# this holds the table created in postGres/terminal
db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://i.pinimg.com/736x/04/8b/8d/048b8dbc061a104f266176b1b7bf828c.jpg"

# user table with data
class User(db.Model):
    """Site user."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)
    
    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"


#model for posts, 
class Post(db.Model):
    """Blog post, user-posts, relationship with User.id"""
    
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    # relationship with User.id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    @property
    def friendly_date(self):
        """returns formated date"""
        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")
    

# connector function to connect this database to app.py
def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)