from flask import Blueprint
from init import db
from models.first_dance import FirstDanceSong
from schemas.first_dance_schema import first_dance_songs_schema

first_dance_bp = Blueprint("firstdance", __name__, url_prefix="/firstdance")

@first_dance_bp.route("/")
def get_all_first_dance_songs():
    stmt = db.select(FirstDanceSong)
    first_dance = db.session.scalars(stmt)
    return first_dance_songs_schema.dump(first_dance)