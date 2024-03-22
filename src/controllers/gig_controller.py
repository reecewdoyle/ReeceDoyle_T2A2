from flask import Blueprint
from init import db
from models.gig import Gig
from schemas.gig_schema import gigs_schema

gig_bp = Blueprint("gigs", __name__, url_prefix=("/gigs"))

@gig_bp.route("/")
def get_all_gigs():
    stmt = db.select(Gig)
    gigs = db.session.scalars(stmt)
    return gigs_schema.dump(gigs)