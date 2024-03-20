from init import ma
from marshmallow import fields

class SongSchema(ma.Schema):
    setlist = fields.Nested("SetlistSchema", only=("id", "name"))

    class Meta:
        fields = ("id", "title", "artist", "genre", "key", "tempo", "setlist")

song_schema = SongSchema()
songs_schema = SongSchema(many=True)
