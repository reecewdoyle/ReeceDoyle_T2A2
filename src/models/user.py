from init import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    # Was going to use this as a method for making a user inactive without deleteing the user. 
    # This is becuase if someone left the "organisation", the gig would still likely be going ahead, therefore you would'nt want to lose the booking. 
    # is_active = db.Column(db.Boolean, default=True)

    agent = db.relationship("Agent", back_populates="user")
    aisle_song = db.relationship("AisleSong", back_populates="user")
    first_dance_song = db.relationship("FirstDanceSong", back_populates="user")
    gigs = db.relationship("Gig", back_populates="user")
    musician = db.relationship("Musician", back_populates="user")
    venue = db.relationship("Venue", back_populates="user")

