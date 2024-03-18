from init import db

class Gigs(db.Model):
    __tablename__ = "gigs"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date) 
    time = db.Column(db.Time)
    invoice = db.Column(db.String(10))

    venue_id = db.Column(db.Integer, db.ForeignKey("venue.id"), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey("agent.id"), nullable=False)
    band_id = db.Column(db.Integer, db.ForeignKey("band.id"), nullable=False)
    setlist_id = db.Column(db.Integer, db.ForeignKey("setlist.id"), nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    user = db.relationship("User", back_populates="gigs")