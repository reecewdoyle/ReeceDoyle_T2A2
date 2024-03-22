from flask import Blueprint
from init import db
from models.venue import Venue
from schemas.venue_schema import venues_schema

venue_bp = Blueprint("venues", __name__, url_prefix="/venues")

@venue_bp.route("/")
def get_all_venues():
    stmt = db.select(Venue)
    venues = db.session.scalars(stmt)
    return venues_schema.dump(venues)