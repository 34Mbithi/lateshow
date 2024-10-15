from . import db
from sqlalchemy.orm import relationship

class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    
    # Relationships
    appearances = db.relationship('Appearance', backref='episode', cascade="all, delete-orphan")

class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)

    # Relationships
    appearances = db.relationship('Appearance', backref='guest', cascade="all, delete-orphan")

class Appearance(db.Model):
    __tablename__ = 'appearances'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    # Validations
    @db.validates('rating')
    def validate_rating(self, key, value):
        if value < 1 or value > 5:
            raise ValueError("Rating must be between 1 and 5.")
        return value
