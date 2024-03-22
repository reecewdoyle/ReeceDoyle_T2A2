from init import ma
from marshmallow import fields

class VenueSchema(ma.Schema):

    user = fields.Nested("UserSchema", only = ["name", "email"])

    class Meta:
        fields = ("id", "title", "manager", "address", "phone", "user")
        ordered = True

venue_schema = VenueSchema()
venues_schema = VenueSchema(many=True)