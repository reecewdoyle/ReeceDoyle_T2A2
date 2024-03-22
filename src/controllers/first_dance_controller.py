from flask import Blueprint
from init import db
from models.first_dance import FirstDanceSong
from schemas.first_dance_schema import first_dance_songs_schema, first_dance_song_schema

first_dance_bp = Blueprint("firstdance", __name__, url_prefix="/firstdance")

@first_dance_bp.route("/")
def get_all_first_dance_songs():
    stmt = db.select(FirstDanceSong)
    first_dance = db.session.scalars(stmt)
    return first_dance_songs_schema.dump(first_dance)

@first_dance_bp.route("/<int:first_dance_song_id>")
def get_first_dance_song(first_dance_song_id):
    stmt = db.select(FirstDanceSong).filter_by(id=first_dance_song_id)
    first_dance = db.session.scalar(stmt)
    if first_dance:
        return first_dance_song_schema.dump(first_dance)
    else:
        return {"error": f"First Dance Song with id {first_dance_song_id} not found"}, 404