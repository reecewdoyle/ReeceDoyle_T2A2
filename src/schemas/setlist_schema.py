from init import ma

class SetlistSchema(ma.Schema):
    class Meta:
        fields = ("id", "song_id", "song_name", "song_type")

setlist_schema = SetlistSchema()
setlists_schema = SetlistSchema(many=True)

