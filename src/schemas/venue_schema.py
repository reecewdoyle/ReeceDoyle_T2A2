from init import ma

class VenueSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "manager", "address", "phone", "gigs")
        fields = ("id", "title", "manager", "address", "phone")

venue_schema = VenueSchema()
venues_schema = VenueSchema(many=True)
