from init import db

class Band(db.Model):
    __tablename__ = 'bands'

    id = db.Column(db.Integer, primary_key=True)

    # Define the secondary relationship with musicians
    musicians = db.relationship('Musician', secondary='band_musician', backref='bands')

class BandMusician(db.Model):
    __tablename__ = 'band_musician'

    band_id = db.Column(db.Integer, db.ForeignKey('bands.id'), primary_key=True)
    musician_id = db.Column(db.Integer, db.ForeignKey('musicians.id'), primary_key=True)


