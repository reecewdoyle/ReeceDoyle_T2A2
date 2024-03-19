from init import ma 

class SongSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "artist", "genre", "key", "tempo")

song_schema = SongSchema()
songs_schema = SongSchema()