from flask import Blueprint
from init import db
from models.aisle import AisleSong 
from schemas.aisle_schema import aisle_songs_schema, aisle_song_schema


aisle_bp = Blueprint("aisle", __name__, url_prefix="/aisle")

@aisle_bp.route("/")
def get_all_aisle_songs():
    stmt =db.select(AisleSong)
    aisle_songs = db.session.scalars(stmt)
    return aisle_songs_schema.dump(aisle_songs)

@aisle_bp.route("/<int:aisle_song_id>")
def get_one_aisle_song(aisle_song_id):
    stmt = db.select(AisleSong).filter_by(id=aisle_song_id)
    aisle_song = db.session.scalar(stmt)
    if aisle_song:
        return aisle_song_schema.dump(aisle_song)
    else:
        return {"error": f"Aisle song with id {aisle_song_id} not found"}, 404