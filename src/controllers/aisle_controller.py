from flask import Blueprint
from init import db
from models.aisle import AisleSong 
from schemas.aisle_schema import aisle_songs_schema


aisle_bp = Blueprint("aisle", __name__, url_prefix="/aisle")

@aisle_bp.route("/")
def get_all_aisle_songs():
    stmt =db.select(AisleSong)
    aisle_songs = db.session.scalars(stmt)
    return aisle_songs_schema.dump(aisle_songs)