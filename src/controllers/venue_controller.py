from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

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

@venue_bp.route("/", methods=["POST"])
@jwt_required()
def create_venue():
    body_data = request.get_json()
    venue = Venue(
        title=body_data.get("title"),
        manager=body_data.get("manager"),
        address=body_data.get("address"),
        phone=body_data.get("phone"),
        user_id = get_jwt_identity()
    )
    db.session.add(venue)
    db.session.commit()
    return venue_schema.dump(venue)

@venue_bp.route("<int:venue_id>", methods=["DELETE"])
def delete_venue(venue_id):
    stmt = db.select(Venue).where(Venue.id == venue_id)
    venue = db.session.scalar(stmt)
    if venue:
        db.session.delete(venue)
        db.session.commit()
        return {"message": f"Venue {venue.title} deleted successfully"}
    else:
        return {"error": f"Venue {venue_id} was not found"}, 404
    
@venue_bp.route("/<int:venue_id>", methods=["PUT", "PATCH"])
def update_venue(venue_id):
    body_data = request.get_json()
    stmt = db.select(Venue).filter_by(id=venue_id)
    venue = db.session.scalar(stmt)
    if venue:
        venue.title = body_data.get("title") or venue.title
        venue.manager = body_data.get("manager") or venue.manager
        venue.address = body_data.get("address") or venue.address
        venue.phone = body_data.get("phone") or venue.phone

        db.session.commit()
        return venue_schema.dump(venue)
    else:
        return {"error": f"Venue with id {venue_id} not found"}, 404