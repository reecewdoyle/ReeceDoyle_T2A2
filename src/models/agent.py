from init import db

class Agent(db.Model):
    __tablename__ = 'agent'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)

    gigs = db.relationship("Gig", back_populates="agent")