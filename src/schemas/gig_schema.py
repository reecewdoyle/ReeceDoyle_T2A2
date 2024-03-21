from init import ma
from marshmallow import fields
from agent_schema import AgentSchema  # Importing AgentSchema for nested serialization
from musician_schema import MusicianSchema  # Importing MusicianSchema for nested serialization
from venue_schema import VenueSchema  # Importing VenueSchema for nested serialization
from user_schema import UserSchema  # Importing UserSchema for nested serialization

class GigSchema(ma.Schema):
    agent = fields.Nested(AgentSchema, only=["name", "phone", "email"])
    user = fields.Nested(UserSchema, only=["name", "email"])
    musician1 = fields.Nested(MusicianSchema, only=["name", "instrument"])
    musician2 = fields.Nested(MusicianSchema, only=["name", "instrument"])
    musician3 = fields.Nested(MusicianSchema, only=["name", "instrument"])
    musician4 = fields.Nested(MusicianSchema, only=["name", "instrument"])
    musician5 = fields.Nested(MusicianSchema, only=["name", "instrument"])
    venue = fields.Nested(VenueSchema, only=["title", "address"])

    class Meta:
        fields = ("id", "date", "time", "invoice", "venue", "agent", "setlist", "user", "musician1", "musician2", "musician3", "musician4", "musician5")

gig_schema = GigSchema()
gigs_schema = GigSchema(many=True)
