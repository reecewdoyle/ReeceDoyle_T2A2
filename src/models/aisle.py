from init import db

class AisleSong(db.Model):
    __tablename__ = 'aisle_song'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    key = db.Column(db.String(6), nullable=False)
    tempo = db.Column(db.Integer, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    user = db.relationship("User", back_populates="aisle_song")
    gigs = db.relationship('Gig', back_populates='aisle_song')

