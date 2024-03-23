from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

from init import ma

class VenueSchema(ma.Schema):

    title = fields.String(required= True, validate=And(
        Length(min=2, error="Title must be at least 2 characters long"),
        Regexp('^[a-zA-Z0-9 ]+$', error="Title can only have alphanumeric characters")
    ))

    manager = fields.String(required= True, validate=And(
        Length(min=2, error="Manager must be at least 2 characters long"),
        Regexp('^[a-zA-Z0-9 ]+$', error="Manager can only have alphanumeric characters")
    ))

    address = fields.String(required=True, validate=And(
        Length(min=10, error="Must enter a valid address"),
        Regexp('^[a-zA-Z0-9\s\.,#-]+$', error="Address can only have alphanumeric characters and certain special characters allowed in an address")
    ))

    phone = fields.String(required= True, validate=And(
        Length(min=10, error="Phone number must be at least 10 numbers long"),
        Regexp('^(?:\+?(61))? ?(?:\((?=.*\)))?(0?[2-57-8])\)? ?(\d\d(?:[- ](?=\d{3})|(?!\d\d[- ]?\d[- ]))\d\d[- ]?\d[- ]?\d{3})$', error="Must enter a valid phone number")
    ))

    user = fields.Nested("UserSchema", only = ["name", "email"])

    class Meta:
        fields = ("id", "title", "manager", "address", "phone", "user")
        ordered = True

venue_schema = VenueSchema()
venues_schema = VenueSchema(many=True)