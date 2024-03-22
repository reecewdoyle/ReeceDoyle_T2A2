from flask import Blueprint
from init import db
from models.agent import Agent
from schemas.agent_schema import agents_schema


agent_bp = Blueprint("agent", __name__, url_prefix="/agent")

@agent_bp.route("/")
def get_all_agents():
    stmt = db.select(Agent)
    agents = db.session.scalars(stmt)
    return agents_schema.dump(agents)
