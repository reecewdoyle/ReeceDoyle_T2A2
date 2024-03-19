from init import ma 

class MusicianSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "phone", "Instrument 1", "Instrument 2", "Instrument 3")

musician_schema = MusicianSchema()
musicians_schema = MusicianSchema(many=True)