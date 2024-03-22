from flask import Blueprint
from init import db
from models.venue import Venue
from schemas.venue_schema import venues_schema, venue_schema

venue_bp = Blueprint("venues", __name__, url_prefix="/venues")

@venue_bp.route("/")
def get_all_venues():
    stmt = db.select(Venue)
    venues = db.session.scalars(stmt)
    return venues_schema.dump(venues)

@venue_bp.route("/<int:venue_id>")
def get_one_venue(venue_id):
    stmt = db.select(Venue).filter_by(id=venue_id)
    venue = db.session.scalar(stmt)
    if venue:
        return venue_schema.dump(venue)
    else:
        return {"error": f"Agent with id {venue_id} not found"}, 404