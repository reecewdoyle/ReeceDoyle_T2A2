from init import ma 

class MusicianSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "phone", "instrument_1", "instrument_2", "instrument_3")

musician_schema = MusicianSchema()
musicians_schema = MusicianSchema(many=True)