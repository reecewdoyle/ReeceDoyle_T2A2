from init import db

class Musician(db.Model):
    __tablename__ = 'musician'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    instrument1 = db.Column(db.String, nullable=False)
    instrument2 = db.Column(db.String)
    instrument3 = db.Column(db.String)
