from init import ma
from marshmallow import fields

class UserSchema(ma.Schema):

    gig = fields.List(fields.Nested("GigSchema", exclude=["user"]))

    class Meta:
        fields = ("id", "name", "email", "password", "is_admin", "gig")

user_schema = UserSchema(exclude=["password"])
users_schema = UserSchema(many=True, exclude=["password"])