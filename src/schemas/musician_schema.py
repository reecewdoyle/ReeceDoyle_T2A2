from init import ma

class MusicianSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "instrument", "email", "phone")
        ordered = True

musician_schema = MusicianSchema()
musicians_schema = MusicianSchema(many=True)

