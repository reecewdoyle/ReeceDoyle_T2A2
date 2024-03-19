from init import ma

class BandSchema(ma.Schema):
    class Meta:
        fields = ("id", "instrument", "musician_id")

band_schema = BandSchema()
bands_schema = BandSchema(many=True)
