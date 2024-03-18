from init import ma
from marshmallow import fields

class UserSchema (ma.Schema):

    gigs = fields.List(fields.Nested("GigsSchema", exclude=["user"]))

    class Meta:
        fields = ("id", "name", "email", "password", "is_admin", "gigs")

user_schema = UserSchema(exclude=["password"]) # will serialise a single user schema
users_schema = UserSchema(many=True, exclude=["password"]) # will serialise a list of users schemas