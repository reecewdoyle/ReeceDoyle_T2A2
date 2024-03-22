from init import ma
from marshmallow import fields

class AisleSongSchema(ma.Schema):

    user = fields.Nested("UserSchema", only = ["name", "email"])

    class Meta:
        fields = ("id", "title", "artist", "genre", "key", "tempo", "user")
        ordered = True

aisle_song_schema = AisleSongSchema()
aisle_songs_schema = AisleSongSchema(many=True)