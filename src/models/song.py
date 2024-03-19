from init import db

class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    key = db.Column(db.String(6), nullable=False)
    tempo = db.Column(db.Integer, nullable=False)