from init import ma

class AgentSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "name", "email", "phone")
        ordered = True
        
agent_schema = AgentSchema()
agents_schema = AgentSchema(many=True)