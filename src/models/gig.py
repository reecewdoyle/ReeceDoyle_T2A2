from init import db

class Gig(db.Model):
    __tablename__ = "gig"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date) 
    time = db.Column(db.Time)
    invoice = db.Column(db.String(10))
    # Foreign keys
    venue_id = db.Column(db.Integer, db.ForeignKey("venue.id"), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey("agent.id"), nullable=False)
    band_id = db.Column(db.Integer, db.ForeignKey("bands.id"), nullable=False)
    setlist_id = db.Column(db.Integer, db.ForeignKey("setlists.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    # Relationships
    # One-to-many relationship with Agent
    agent = db.relationship("Agent", back_populates="gigs")
    # One-to-many relationship with Venue
    venue = db.relationship("Venue", back_populates="gigs")
    # One-to-many relationship with User
    user = db.relationship("User", back_populates="gigs")
    # Many-to-one relationship with Band
    band = db.relationship("Band", back_populates="gigs")
    # One-to-many relationship with Setlist
    setlist = db.relationship("Setlist", back_populates="gigs")


