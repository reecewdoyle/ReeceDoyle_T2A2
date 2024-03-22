from init import db

class Musician(db.Model):
    __tablename__ = 'musicians'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    instrument = db.Column(db.String, nullable=False)

    gigs = db.relationship("Gig", back_populates="musician")

    # Define the reverse relationships with Gig
    # gigs_as_musician1 = db.relationship("Gig", foreign_keys="[Gig.musician1_id]")
    # gigs_as_musician2 = db.relationship("Gig", foreign_keys="[Gig.musician2_id]")
    # gigs_as_musician3 = db.relationship("Gig", foreign_keys="[Gig.musician3_id]")
    # gigs_as_musician4 = db.relationship("Gig", foreign_keys="[Gig.musician4_id]")
    # gigs_as_musician5 = db.relationship"Gig", foreign_keys="[Gig.musician5_id]")
