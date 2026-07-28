from server import db
from flask import current_app
from enum import Enum
from server.models.dtos.message_dto import MessageDTO, MessagesDTO
from server.models.postgis.user import User
from server.models.postgis.task import Task
from server.models.postgis.project import Project
from server.models.postgis.utils import timestamp
from server.models.postgis.utils import NotFound
""" Describes the various kinds of messages a user might receive """
SYSTEM = 1
BROADCAST = 2
MENTION_NOTIFICATION = 3
VALIDATION_NOTIFICATION = 4
INVALIDATION_NOTIFICATION = 5
""" Describes an individual Message a user can send """
__tablename__ = 'messages'
__table_args__ = db.ForeignKeyConstraint(['task_id', 'project_id'], [
    'tasks.id', 'tasks.project_id']),
id = db.Column(db.Integer, primary_key=True)
message = db.Column(db.String)
subject = db.Column(db.String)
from_user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'))
to_user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), index=True)
project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), index=True)
task_id = db.Column(db.Integer, index=True)
message_type = db.Column(db.Integer, index=True)
date = db.Column(db.DateTime, default=timestamp)
read = db.Column(db.Boolean, default=False)
from_user = db.relationship(User, foreign_keys=[from_user_id])
to_user = db.relationship(User, foreign_keys=[to_user_id], backref='messages')
project = db.relationship(Project, foreign_keys=[project_id], backref=
    'messages')
task = db.relationship(Task, primaryjoin=
    'and_(Task.id == foreign(Message.task_id), Task.project_id == Message.project_id)'
    , backref='messages')
@classmethod...
"""docstring"""
message = cls()
message.subject = dto.subject
message.message = dto.message
message.from_user_id = dto.from_user_id
message.to_user_id = to_user_id
message.project_id = dto.project_id
message.task_id = dto.task_id
if dto.message_type is not None:
message.message_type = MessageType(dto.message_type)
return message
