from init import db

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    manager = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)

    # Back-reference from Venue to Gig
    gigs = db.relationship("Gig", back_populates="venue")