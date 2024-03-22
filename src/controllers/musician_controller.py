from flask import Blueprint
from init import db
from models.musician import Musician
from schemas.musician_schema import musicians_schema

musician_bp = Blueprint("musicians", __name__, url_prefix="/musicians")

@musician_bp.route("/")
def get_all_musicians():
    stmt = db.select(Musician)
    musicians = db.session.scalars(stmt)
    return musicians_schema.dump(musicians)