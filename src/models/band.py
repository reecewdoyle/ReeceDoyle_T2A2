from init import db
from .band_musician import band_musician  # Make sure to import the join table correctly

class Band(db.Model):
    __tablename__ = 'bands'

    id = db.Column(db.Integer, primary_key=True)

    # Define the secondary relationship with musicians using the association table
    musicians = db.relationship('Musician', secondary=band_musician, back_populates='bands')

    # Define the one-to-many relationship with Gig
    gigs = db.relationship('Gig', back_populates='band')


