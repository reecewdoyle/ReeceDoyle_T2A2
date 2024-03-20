from init import ma
from marshmallow import fields, validates_schema, ValidationError

VALID_SONG_TYPES = ("Ceremony", "Cocktail Hour", "First Dance", "Party")

class SetlistSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    song_type = fields.String(required=True)

    @validates_schema
    def validate_song_type(self, data, **kwargs):
        song_type = data.get('song_type')
        if song_type not in VALID_SONG_TYPES:
            raise ValidationError(f"Invalid song type: {song_type}. Allowed types are: {', '.join(VALID_SONG_TYPES)}")

setlist_schema = SetlistSchema()
setlists_schema = SetlistSchema(many=True)
