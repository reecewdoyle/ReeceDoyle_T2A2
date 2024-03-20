from init import ma
from marshmallow import fields
from agent_schema import AgentSchema  # Importing AgentSchema for nested serialisation

class GigSchema(ma.Schema):
    agent = fields.Nested(AgentSchema, only=["name", "phone", "email"])
    user = fields.Nested("UserSchema", only=["name", "email"])

    class Meta:
        fields = ("id", "date", "time", "invoice", "venue", "agent", "band", "setlist", "user")

gig_schema = GigSchema()
gigs_schema = GigSchema(many=True)
