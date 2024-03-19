from init import db

class Band(db.Model):
    __tablename__ = 'band'

    id = db.Column(db.Integer, primary_key=True)
    instrument = db.Column(db.String, nullable=False)

    musician_id = db.Column(db.Integer, db.ForeignKey("musicians.id"), nullable=False)