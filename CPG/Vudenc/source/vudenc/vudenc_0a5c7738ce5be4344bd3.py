@staticmethod...
"""docstring"""
return Message.query.filter(Message.to_user_id == user_id, Message.read == 
    False).count()
