from init import ma

class MusicianSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "phone", "instrument")

musician_schema = MusicianSchema()
musicians_schema = MusicianSchema(many=True)

