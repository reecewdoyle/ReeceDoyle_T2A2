from init import ma

class FirstDanceSongSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "artist", "genre", "key", "tempo")
        ordered = True
        
first_dance_song_schema = FirstDanceSongSchema()
first_dance_songs_schema = FirstDanceSongSchema(many=True)
