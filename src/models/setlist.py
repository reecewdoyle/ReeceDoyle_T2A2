from init import db

class Setlist(db.Model):
    __tablename__ = 'setlist'

    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    song_name = db.Column(db.Integer, db.ForeignKey('song.name'), nullable=False)
    song_type = db.Column(db.String, nullable=False)