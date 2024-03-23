from marshmallow import fields
from marshmallow.validate import Length, And, Regexp, OneOf

from init import ma

VALID_INSTRUMENTS = ("Guitar", "Bass", "Drums", "Vocals", "Keyboards", "Saxophone", "Trumpet", "Trombone", "Violin", "Cello", "Kazoo", "Flute", "Clarinet", "Harp", "Banjo", "Mandolin", "Accordion", "Harmonica", "Synthesizer", "Ukulele")

class MusicianSchema(ma.Schema):

    name = fields.String(required= True, validate=And(
        Length(min=2, error="Name must be at least 2 characters long"),
        Regexp('^[a-zA-Z0-9 ]+$', error="Name can only have alphanumeric characters")
    ))

    instrument =fields.String(validate=OneOf(VALID_INSTRUMENTS))

    email = fields.String(required= True, validate=And(
        Length(min=2, error="Title must be at least 2 characters long"),
        Regexp('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', error="Must enter a valid email address")
    ))

    phone = fields.String(required= True, validate=And(
        Length(min=10, error="Phone number must be at least 10 numbers long"),
        Regexp('^(?:\+?(61))? ?(?:\((?=.*\)))?(0?[2-57-8])\)? ?(\d\d(?:[- ](?=\d{3})|(?!\d\d[- ]?\d[- ]))\d\d[- ]?\d[- ]?\d{3})$', error="Must enter a valid phone number")
    ))

    user = fields.Nested("UserSchema", only = ["name", "email"])

    class Meta:
        fields = ("id", "name", "instrument", "email", "phone", "user")
        ordered = True

musician_schema = MusicianSchema()
musicians_schema = MusicianSchema(many=True)