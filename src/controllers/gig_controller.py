from flask import Blueprint
from init import db
from models.gig import Gig
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