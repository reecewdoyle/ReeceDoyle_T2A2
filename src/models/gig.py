from init import db

class Gig(db.Model):
    __tablename__ = "gig"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date) 
    time = db.Column(db.Time)
    invoice = db.Column(db.String(10))
    venue_id = db.Column(db.Integer, db.ForeignKey("venue.id"), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey("agent.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    musician_id = db.Column(db.Integer, db.ForeignKey("musician.id"), nullable=False)
    first_dance_song_id = db.Column(db.Integer, db.ForeignKey("first_dance_song.id"), nullable=True)
    aisle_song_id = db.Column(db.Integer, db.ForeignKey("aisle_song.id"), nullable=True)
    
    # Relationships
    agent = db.relationship("Agent", back_populates="gigs")
    venue = db.relationship("Venue", back_populates="gigs")
    user = db.relationship("User", back_populates="gigs")
    musician =  db.relationship("Musician", back_populates="gigs")
    first_dance_song = db.relationship("FirstDanceSong", back_populates="gigs",)
    aisle_song = db.relationship("AisleSong", back_populates="gigs")