from init import ma

class AisleSongSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "artist", "genre", "key", "tempo")

song_schema = AisleSongSchema()
songs_schema = AisleSongSchema(many=True)