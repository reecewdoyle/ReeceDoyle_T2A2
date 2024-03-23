from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.first_dance import FirstDanceSong
from models.user import User
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
    
@first_dance_bp.route("/", methods=["POST"])
@jwt_required()
def create_first_dance_song():
    body_data = first_dance_song_schema.load(request.get_json())
    first_dance_song = FirstDanceSong(
        title=body_data.get("title"),
        artist=body_data.get("artist"),
        genre=body_data.get("genre"),
        key=body_data.get("key"),
        tempo=body_data.get("tempo"),
        user_id = get_jwt_identity()
    )
    db.session.add(first_dance_song)
    db.session.commit()
    return first_dance_song_schema.dump(first_dance_song)

@first_dance_bp.route("/<int:first_dance_song_id>", methods=["DELETE"])
def delete_fist_dance_song(first_dance_song_id):
    is_admin = is_user_admin()
    if not is_admin:
        return {"error": "Not authorised to delete an first dance song"}, 403
    stmt = db.select(FirstDanceSong).where(FirstDanceSong.id == first_dance_song_id)
    first_dance_song = db.session.scalar(stmt)
    if first_dance_song:
        db.session.delete(first_dance_song)
        db.session.commit()
        return {"message": f"First Dance Song with {first_dance_song.title} deleted successfully"}
    else:
        return {"message": f"First dance song with {first_dance_song_id} was not forund"}, 404
    
@first_dance_bp.route("/<int:first_dance_song_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_first_dance_song(first_dance_song_id):
    body_data = first_dance_song_schema.load(request.get_json(), partial=True)
    stmt = db.select(FirstDanceSong).filter_by(id=first_dance_song_id)
    first_dance_song = db.session.scalar(stmt)
    if first_dance_song:
        if str(first_dance_song.user_id) != get_jwt_identity():
            return {"error": "Only the owner can edit the first dance song data"}, 403
        first_dance_song.title = body_data.get("title") or first_dance_song.title
        first_dance_song.artist = body_data.get("artist") or first_dance_song.artist
        first_dance_song.genre = body_data.get("genre") or first_dance_song.genre
        first_dance_song.key = body_data.get("key") or first_dance_song.key
        first_dance_song.tempo = body_data.get("tempo") or first_dance_song.tempo

        db.session.commit()
        return first_dance_song_schema.dump(first_dance_song)
    else:
        return {"error": f"First Dance Song with id {first_dance_song_id} not found"}, 404

def is_user_admin():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    return user.is_admin
