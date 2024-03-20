from init import db

class Setlist(db.Model):
    __tablename__ = 'setlists'

    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), nullable=False)
    song_type = db.Column(db.String, nullable=False)

    # Define the relationship with Gig
    gigs = db.relationship('Gig', back_populates='setlist')