from init import ma
from marshmallow import fields

class GigsSchema(ma.Schema):
    user = fields.Nested("UserSchema", only = ["name", "email"])
    class Meta:
        fields = ("id", "date", "time", "invoice", "venue", "agent", "band", "setlist", "user")

gig_schema = GigsSchema()
gigs_schema = GigsSchema(many=True)