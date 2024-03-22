from init import ma
# from marshmallow import fields
# from gig_schema import GigSchema  # Importing GigSchema for nested serialization

class VenueSchema(ma.Schema):
    # gigs = fields.Nested(GigSchema, many=True, exclude=["venue"])

    class Meta:
        # fields = ("id", "title", "manager", "address", "phone", "gigs")
        fields = ("id", "title", "manager", "address", "phone")

venue_schema = VenueSchema()
venues_schema = VenueSchema(many=True)
