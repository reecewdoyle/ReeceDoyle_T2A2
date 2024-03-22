from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.agent import Agent
from schemas.agent_schema import agents_schema, agent_schema


agent_bp = Blueprint("agent", __name__, url_prefix="/agent")

@agent_bp.route("/")
def get_all_agents():
    stmt = db.select(Agent)
    agents = db.session.scalars(stmt)
    return agents_schema.dump(agents)

@agent_bp.route("/<int:agent_id>")
def get_one_agent(agent_id):
    stmt = db.select(Agent).filter_by(id=agent_id)
    agent = db.session.scalar(stmt)
    if agent:
        return agent_schema.dump(agent)
    else:
        return {"error": f"Agent with id {agent_id} not found"}, 404
    
@agent_bp.route("/", methods=["POST"])
@jwt_required()
def create_agent():
    body_data = request.get_json()
    agent = Agent(
        title=body_data.get("title"),
        name=body_data.get("name"),
        email=body_data.get("email"),
        phone=body_data.get("phone"),
        user_id = get_jwt_identity()
    )
    db.session.add(agent)
    db.session.commit()
    return agent_schema.dump(agent)