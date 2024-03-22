from flask import Blueprint
from init import db
from models.musician import Musician
from schemas.musician_schema import musicians_schema, musician_schema

musician_bp = Blueprint("musicians", __name__, url_prefix="/musicians")

@musician_bp.route("/")
def get_all_musicians():
    stmt = db.select(Musician)
    musicians = db.session.scalars(stmt)
    return musicians_schema.dump(musicians)

@musician_bp.route("/<int:musician_id>")
def get_one_musician(musician_id):
    stmt = db.select(Musician).filter_by(id=musician_id)
    musician = db.session.scalar(stmt)
    if musician:
        return musician_schema.dump(musician)
    else:
        return {"error": f"Agent with id {musician_id} not found"}, 404