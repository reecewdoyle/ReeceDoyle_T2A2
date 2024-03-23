from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.musician import Musician
from models.user import User
from schemas.musician_schema import musicians_schema, musician_schema


musician_bp = Blueprint("musician", __name__, url_prefix="/musician")

@musician_bp.route("/")
def get_all_musician():
    stmt = db.select(Musician)
    musician = db.session.scalars(stmt)
    return musicians_schema.dump(musician)

@musician_bp.route("/<int:musician_id>")
def get_one_musician(musician_id):
    stmt = db.select(Musician).filter_by(id=musician_id)
    musician = db.session.scalar(stmt)
    if musician:
        return musician_schema.dump(musician)
    else:
        return {"error": f"Agent with id {musician_id} not found"}, 404
    
@musician_bp.route("/", methods=["POST"])
@jwt_required()
def create_musician():
    body_data = musician_schema.load(request.get_json())
    musician = Musician(
        name=body_data.get("name"),
        instrument=body_data.get("instrument"),
        email=body_data.get("email"),
        phone=body_data.get("phone"),
        user_id = get_jwt_identity()
    )
    db.session.add(musician)
    db.session.commit()
    return musician_schema.dump(musician)

@musician_bp.route("/<int:musician_id>", methods=["DELETE"])
@jwt_required()
def delete_musician(musician_id):
    is_admin = is_user_admin()
    if not is_admin:
        return {"error": "Not authorised to delete a musician"}, 403
    stmt = db.select(Musician).where(Musician.id ==musician_id)
    musician = db.session.scalar(stmt)
    if musician:
        db.session.delete(musician)
        db.session.commit()
        return {"message": f"Musician {musician.name} deleted successfully"}
    else:
        return {"message": f"Musician {musician_id} was not found"}, 404
    
@musician_bp.route("/<int:musician_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_musician(musician_id):
    body_data = musician_schema.load(request.get_json(), partial=True)
    stmt = db.select(Musician).filter_by(id=musician_id)
    musician = db.session.scalar(stmt)
    if musician:
        if str(musician.user_id) != get_jwt_identity():
            return {"error": "Only the owner can edit musician data"}, 403
        musician.name = body_data.get("name") or musician.name
        musician.email = body_data.get("email") or musician.email
        musician.phone = body_data.get("phone") or musician.phone
        musician.instrument = body_data.get("instrument") or musician.instrument

        db.session.commit()
        return musician_schema.dump(musician)
    else:
        return {"error": f"Musician with id {musician_id} not found"}, 404

def is_user_admin():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    return user.is_admin