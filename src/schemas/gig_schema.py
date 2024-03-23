from init import ma
from marshmallow import fields

class GigSchema(ma.Schema):
    agent = fields.Nested("AgentSchema", only=["name", "phone", "email"])
    user = fields.Nested("UserSchema", only=["name", "email"])
    musician = fields.Nested("MusicianSchema", only=["name", "instrument"])
    venue = fields.Nested("VenueSchema", only=["title", "address"])
    aisle_song = fields.Nested("AisleSongSchema", only=["title", "key", "tempo"])
    first_dance_song = fields.Nested("FirstDanceSongSchema", only=["title", "key", "tempo"])

    class Meta:
        fields = ("id", "date", "time", "invoice", "venue", "agent", "user", "musician", "aisle_song", "first_dance_song")
        ordered = True

gig_schema = GigSchema()
gigs_schema = GigSchema(many=True)

