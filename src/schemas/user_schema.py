from init import ma
from marshmallow import fields

class UserSchema(ma.Schema):

    agent = fields.List(fields.Nested("AgentSchema", exclude=["user"]))
    aisle_song = fields.List(fields.Nested("AisleSongSchema", exclude=["user"]))
    first_dance_song = fields.List(fields.Nested("FirstDanceSongSchema", exclude=["user"]))
    gig = fields.List(fields.Nested("GigSchema", exclude=["user"]))
    musicians = fields.List(fields.Nested("MusicianSchema", exclude=["user"]))
    venue = fields.List(fields.Nested("VenueSchema", exclude=["venue"]))

    class Meta:
        fields = ("id", "name", "email", "password", "is_admin", "gig", "agent", "aisle_song", "first_dance_song", "musicians", "venue")

user_schema = UserSchema(exclude=["password"])
users_schema = UserSchema(many=True, exclude=["password"])