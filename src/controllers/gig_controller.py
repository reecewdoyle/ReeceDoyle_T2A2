from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.gig import Gig
from models.user import User
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
    body_data = gig_schema.load(request.get_json())
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
@jwt_required()
def delete_gig(gig_id):
    is_admin = is_user_admin()
    if not is_admin:
        return {"error": "Not authorised to delete a gig"}, 403
    stmt = db.select(Gig).where(Gig.id == gig_id)
    gig = db.session.scalar(stmt)
    if gig:
        db.session.delete(gig)
        db.session.commit()
        return {"message": f"Gig on {gig.date} deleted successfully"}
    else:
        return {"message": f"Gig with {gig_id} was not found"}, 404
    
@gig_bp.route("/<int:gig_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_gig(gig_id):
    body_data = gig_schema.load(request.get_json(), partial=True)
    stmt = db.select(Gig).filter_by(id=gig_id)
    gig = db.session.scalar(stmt)
    if gig:
        if str(gig.user_id) != get_jwt_identity():
            return {"error": "Only the owner can edit the gig data"}, 403
        gig.date = body_data.get("date") or gig.date
        gig.time = body_data.get("time") or gig.time
        gig.invoice = body_data.get("invoice") or gig.invoice
        gig.venue_id = body_data.get("venue_id") or gig.venue_id
        gig.agent_id = body_data.get("agent_id") or gig.agent_id
        gig.user_id = body_data.get("user_id") or gig.user_id
        gig.musician_id = body_data.get("musician_id") or gig.musician_id
        gig.first_dance_song_id = body_data.get("first_dance_song_id") or gig.first_dance_song_id
        gig.aisle_song_id = body_data.get("aisle_song_id") or gig.aisle_song_id

        db.session.commit()
        return gig_schema.dump(gig)
    else:
        return {"error": f"Gig with id {gig_id} not found"}, 404
    
def is_user_admin():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    return user.is_admin
