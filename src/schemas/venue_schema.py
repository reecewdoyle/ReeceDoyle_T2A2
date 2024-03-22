from init import ma

class VenueSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "manager", "address", "phone")
        ordered = True

venue_schema = VenueSchema()
venues_schema = VenueSchema(many=True)
