@staticmethod...
"""docstring"""
Message.query.filter(Message.to_user_id == user_id, Message.id.in_(message_ids)
    ).delete(synchronize_session=False)
db.session.commit()
