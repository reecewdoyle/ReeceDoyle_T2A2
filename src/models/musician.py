from init import db
from .band_musician import band_musician

class Musician(db.Model):
    __tablename__ = 'musicians'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    instrument = db.Column(db.String, nullable=False)

    # Define the relationship with bands using the association table
    bands = db.relationship('Band', secondary=band_musician, back_populates='musicians')
