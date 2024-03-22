from init import db

class FirstDanceSong(db.Model):
    __tablename__ = 'first_dance_song'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    key = db.Column(db.String, nullable=False)
    tempo = db.Column(db.Integer, nullable=False)

    gigs = db.relationship("Gig", back_populates='first_dance_song')