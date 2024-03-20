from init import db

class Band(db.Model):
    __tablename__ = 'bands'

    id = db.Column(db.Integer, primary_key=True)

    # Define the secondary relationship with musicians using the association table
    musicians = db.relationship('Musician', secondary='band_musician', backref='bands')




