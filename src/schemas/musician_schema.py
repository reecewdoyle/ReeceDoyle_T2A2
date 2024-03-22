from init import ma
from marshmallow import fields

class MusicianSchema(ma.Schema):

    user = fields.Nested("UserSchema", only = ["name", "email"])

    class Meta:
        fields = ("id", "name", "instrument", "email", "phone", "user")
        ordered = True

musician_schema = MusicianSchema()
musicians_schema = MusicianSchema(many=True)

