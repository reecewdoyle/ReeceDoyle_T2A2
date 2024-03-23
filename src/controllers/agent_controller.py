import functools

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.agent import Agent
from models.user import User
from schemas.agent_schema import agents_schema, agent_schema


agent_bp = Blueprint("agent", __name__, url_prefix="/agent")

def authorise_as_admin(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        stmt = db.select(User).filter_by(id=user_id)
        user = db.session.scalar(stmt)
        # if the user is an admin
        if user.is_admin:
            # we will continue and run the decorated function
            return fn(*args, **kwargs)
        # else (if the user is NOT an admin)
        else:
            # return an error 
            return {"error": "Not authorised to delete an agent"}, 403
    
    return wrapper

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
@authorise_as_admin
def create_agent():
    body_data = agent_schema.load(request.get_json())
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

@agent_bp.route("/<int:agent_id>", methods=["DELETE"])
@jwt_required()
@authorise_as_admin
def delete_agent(agent_id):
    # is_admin = is_user_admin()
    # if not is_admin:
    #     return {"error": "Not authorised to delete an agent"}, 403
    stmt = db.select(Agent).where(Agent.id == agent_id)
    agent = db.session.scalar(stmt)
    if agent:
        db.session.delete(agent)
        db.session.commit()
        return {"message": f"Agent {agent.name} deleted successfully"}
    else:
        return {"error": f"Agent with {agent_id} was not found"}, 404


@agent_bp.route("/<int:agent_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_agent(agent_id):
    body_data = agent_schema.load(request.get_json(), partial=True)
    stmt = db.select(Agent).filter_by(id=agent_id)
    agent = db.session.scalar(stmt)
    if agent:
        if str(agent.user_id) != get_jwt_identity():
            return {"error": "Only the owner can edit the agent data"}, 403
        agent.title = body_data.get("title") or agent.title
        agent.name = body_data.get("name") or agent.name
        agent.email = body_data.get("email") or agent.email
        agent.phone = body_data.get("phone") or agent.phone

        db.session.commit()
        return agent_schema.dump(agent)
    else:
        return {"error": f"Agent with id {agent_id} not found"}, 404
    

