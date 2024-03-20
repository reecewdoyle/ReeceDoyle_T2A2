from init import ma
from .musician_schema import MusicianSchema

class BandSchema(ma.Schema):
    musician = ma.Nested(MusicianSchema(only=("name", "instrument")))

    class Meta:
        fields = ("id", "musician")

band_schema = BandSchema()
bands_schema = BandSchema(many=True)
