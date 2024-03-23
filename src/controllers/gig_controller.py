from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.gig import Gig
from schemas.gig_schema import gigs_schema, gig_schema

gig_bp = Blueprint("gigs", __name__, url_prefix=("/gigs"))

@gig_bp.route("/")
def get_all_gigs():
    stmt = db.select(Gig)
    gigs = db.session.scalars(stmt)
    return gigs_schema.dump(gigs)

@gig_bp.route("/<int:gig_id>")
def get_one_gig(gig_id):
    stmt = db.select(Gig).filter_by(id=gig_id)
    gig = db.session.scalar(stmt)
    if gig:
        return gig_schema.dump(gig)
    else:
        return {"error": f"Agent with id {gig_id} not found"}, 404

@gig_bp.route("/", methods=["POST"])
@jwt_required()
def create_gig():
    body_data = request.get_json()
    gig = Gig(
        date=body_data.get("date"),
        time=body_data.get("time"),
        invoice=body_data.get("invoice"),
        venue_id=body_data.get("venue_id"),
        agent_id=body_data.get("agent_id"),
        user_id = get_jwt_identity(),
        musician_id=body_data.get("musician_id"),
        first_dance_song_id=body_data.get("first_dance_song_id"),
        aisle_song_id=body_data.get("aisle_song_id")
    )
    db.session.add(gig)
    db.session.commit()
    return gig_schema.dump(gig)

@gig_bp.route("/<int:gig_id>", methods=["DELETE"])
def delete_gig(gig_id):
    stmt = db.select(Gig).where(Gig.id == gig_id)
    gig = db.session.scalar(stmt)
    if gig:
        db.session.delete(gig)
        db.session.commit()
        return {"message": f"Gig on {gig.date} deleted successfully"}
    else:
        return {"message": f"Gig with {gig_id} was not found"}, 404