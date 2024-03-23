from marshmallow import fields
from marshmallow.validate import Length, And, Regexp, OneOf, Range

from init import ma

VALID_GENRES = ("Rock", "Pop", "Folk", "Country", "Jazz", "Funk", "R&B", "Hip Hop", "Rap", "Metal", "Hard Rock", "Classical")
VALID_KEYS = ("Ab", "Abm", "A", "Am", "A#", "A#m", "Bb", "Bbm", "B", "Bm", "C", "Cm", "C#", "C#m", "Db", "Dbm", "D", "Dm", "D#", "D#m", "Eb", "Ebm", "E", "Em", "F", "Fm", "F#", "F#m", "Gb", "Gbm", "G", "Gm", "G#", "G#m")

class AisleSongSchema(ma.Schema):

    title = fields.String(required= True, validate=And(
        Length(min=2, error="Title must be at least 2 characters long"),
        Regexp('^[a-zA-Z0-9 ]+$', error="Title can only have alphanumeric characters")
    ))

    artist = fields.String(required= True, validate=And(
        Length(min=2, error="Artist must be at least 2 characters long"),
        Regexp('^[a-zA-Z0-9 ]+$', error="Artist can only have alphanumeric characters")
    ))

    genre = fields.String(validate=OneOf(VALID_GENRES))

    key = fields.String(validate=OneOf(VALID_KEYS))

    tempo = fields.Integer(required=True, validate=Range(min=40, max=250, error="Tempo must be between 40 and 250"))


    user = fields.Nested("UserSchema", only = ["name", "email"])

    class Meta:
        fields = ("id", "title", "artist", "genre", "key", "tempo", "user")
        ordered = True

aisle_song_schema = AisleSongSchema()
aisle_songs_schema = AisleSongSchema(many=True)