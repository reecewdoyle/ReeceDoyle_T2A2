from init import ma
from marshmallow import fields

class FirstDanceSongSchema(ma.Schema):

    user = fields.Nested("UserSchema", only = ["name", "email"])

    class Meta:
        fields = ("id", "title", "artist", "genre", "key", "tempo", "user")
        ordered = True

first_dance_song_schema = FirstDanceSongSchema()
first_dance_songs_schema = FirstDanceSongSchema(many=True)