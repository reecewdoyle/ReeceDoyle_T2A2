import os

from flask import Flask
from marshmallow.exceptions import ValidationError

from init import db, ma, bcrypt, jwt 

# The Flask Application
def create_app():
    app = Flask(__name__)

    app.json.sort_keys = False

    # configs 
    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URI")
    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")

    # connect libraries with flask app
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    
    # Error handling

    @app.errorhandler(400)
    def bad_request(err):
        return {"error": str(err)}, 400
    
    @app.errorhandler(404)
    def not_found(err):
        return {"error": str(err)}, 404

    @app.errorhandler(ValidationError)
    def validation_error(error):
        return {"error": error.messages}, 400


    # This is where the Blueptints are registered
    
    from controllers.cli_commands import db_commands
    app.register_blueprint(db_commands)

    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    from controllers.agent_controller import agent_bp
    app.register_blueprint(agent_bp)

    from controllers.aisle_controller import aisle_bp
    app.register_blueprint(aisle_bp)

    from controllers.first_dance_controller import first_dance_bp
    app.register_blueprint(first_dance_bp)

    from controllers.musician_controller import musician_bp
    app.register_blueprint(musician_bp)

    from controllers.venue_controller import venue_bp
    app.register_blueprint(venue_bp)

    from controllers.gig_controller import gig_bp
    app.register_blueprint(gig_bp)

    
    return app