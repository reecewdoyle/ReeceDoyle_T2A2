from init import ma

class FirstDanceSongSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "artist", "genre", "key", "tempo")

song_schema = FirstDanceSongSchema()
songs_schema = FirstDanceSongSchema(many=True)
