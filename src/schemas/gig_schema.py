from init import ma
from marshmallow import fields

class GigSchema(ma.Schema):
    user = fields.Nested("UserSchema", only = ["name", "email"])
    class Meta:
        fields = ("id", "date", "time", "invoice", "venue", "agent", "band", "setlist", "user")

gig_schema = GigSchema()
gigs_schema = GigSchema(many=True)