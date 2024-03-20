from init import db

class Musician(db.Model):
    __tablename__ = 'musicians'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    instrument_1 = db.Column(db.String, nullable=False)
    instrument_2 = db.Column(db.String)
    instrument_3 = db.Column(db.String)