from init import ma

class AisleSongSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "artist", "genre", "key", "tempo")

aisle_song_schema = AisleSongSchema()
aisle_songs_schema = AisleSongSchema(many=True)