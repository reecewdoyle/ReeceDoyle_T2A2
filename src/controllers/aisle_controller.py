from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.aisle import AisleSong
from models.user import User
from schemas.aisle_schema import aisle_songs_schema, aisle_song_schema


aisle_bp = Blueprint("aisle", __name__, url_prefix="/aisle")

@aisle_bp.route("/") # GET /aisle
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
    
@aisle_bp.route("/", methods=["POST"]) # POST /aisle
@jwt_required()
def create_aisle_song():
    body_data = aisle_song_schema.load(request.get_json())
    aisle_song = AisleSong(
        title=body_data.get("title"),
        artist=body_data.get("artist"),
        genre=body_data.get("genre"),
        key=body_data.get("key"),
        tempo=body_data.get("tempo"),
        user_id = get_jwt_identity()
    )
    db.session.add(aisle_song)
    db.session.commit()
    return aisle_song_schema.dump(aisle_song)

@aisle_bp.route("/<int:aisle_song_id>", methods=["DELETE"]) # DELETE /aisle/int:aisle_song_id
@jwt_required()
def delete_aisle_song(aisle_song_id):
    is_admin = is_user_admin()
    if not is_admin:
        return {"error": "Not authorised to delete an agent"}, 403
    stmt = db.select(AisleSong).where(AisleSong.id == aisle_song_id)
    aisle_song = db.session.scalar(stmt)
    if aisle_song:
        db.session.delete(aisle_song)
        db.session.commit()
        return {"message": f"Aisle Song with {aisle_song.title} deleted successfully"}
    else:
        return {"message": f"Aisle Song with {aisle_song_id} was not found"}, 404
    
@aisle_bp.route("/<int:aisle_song_id>", methods=["PUT", "PATCH"]) # PATCH /aisle/int:aisle_song_id
@jwt_required()
def update_aisle_song(aisle_song_id):
    body_data = aisle_song_schema.load(request.get_json(), partial=True)
    stmt = db.select(AisleSong).filter_by(id=aisle_song_id)
    aisle_song = db.session.scalar(stmt)
    if aisle_song:
        if str(aisle_song.user_id) != get_jwt_identity():
            return {"error": "Only yhe owner can edit the aisle song data"}, 403
        aisle_song.title = body_data.get("title") or aisle_song.title
        aisle_song.artist = body_data.get("artist") or aisle_song.artist
        aisle_song.genre = body_data.get("genre") or aisle_song.genre
        aisle_song.key = body_data.get("key") or aisle_song.key
        aisle_song.tempo = body_data.get("tempo") or aisle_song.tempo

        db.session.commit()
        return aisle_song_schema.dump(aisle_song)
    else:
        return {"error": f"Aisle Song with id {aisle_song_id} not found"}, 404
    
def is_user_admin(): # is admin function
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    return user.is_admin