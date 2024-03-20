from init import db

# Association table to define the many-to-many relationship between bands and musicians
band_musician = db.Table('band_musician',
    db.Column('band_id', db.Integer, db.ForeignKey('bands.id'), primary_key=True),
    db.Column('musician_id', db.Integer, db.ForeignKey('musicians.id'), primary_key=True)
)
