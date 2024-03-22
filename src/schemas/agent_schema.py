from init import ma
from marshmallow import fields

class AgentSchema(ma.Schema):

    user = fields.Nested("UserSchema", only = ["name", "email"])
    
    class Meta:
        fields = ("id", "title", "name", "email", "phone", "user")
        ordered = True
        
agent_schema = AgentSchema()
agents_schema = AgentSchema(many=True)