from init import ma

class UserSchema (ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "password", "is_admin")

user_schema = UserSchema(exclude=["password"]) # will serialise a single user schema
users_schema = UserSchema(many=True, exclude=["password"]) # will serialise a list of users schemas