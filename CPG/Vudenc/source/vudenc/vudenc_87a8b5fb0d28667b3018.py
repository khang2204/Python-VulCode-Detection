import geojson
import datetime
import dateutil.parser
from server import db
from sqlalchemy import desc
from server.models.dtos.user_dto import UserDTO, UserMappedProjectsDTO, MappedProject, UserFilterDTO, Pagination, UserSearchQuery, UserSearchDTO, ProjectParticipantUser, ListedUser
from server.models.postgis.licenses import License, users_licenses_table
from server.models.postgis.project_info import ProjectInfo
from server.models.postgis.statuses import MappingLevel, ProjectStatus, UserRole
from server.models.postgis.utils import NotFound, timestamp
""" Describes the history associated with a task """
__tablename__ = 'users'
id = db.Column(db.BigInteger, primary_key=True, index=True)
validation_message = db.Column(db.Boolean, default=True, nullable=False)
username = db.Column(db.String, unique=True)
role = db.Column(db.Integer, default=0, nullable=False)
mapping_level = db.Column(db.Integer, default=1, nullable=False)
projects_mapped = db.Column(db.Integer, default=1, nullable=False)
tasks_mapped = db.Column(db.Integer, default=0, nullable=False)
tasks_validated = db.Column(db.Integer, default=0, nullable=False)
tasks_invalidated = db.Column(db.Integer, default=0, nullable=False)
projects_mapped = db.Column(db.ARRAY(db.Integer))
email_address = db.Column(db.String)
is_email_verified = db.Column(db.Boolean, default=False)
is_expert = db.Column(db.Boolean, default=False)
twitter_id = db.Column(db.String)
facebook_id = db.Column(db.String)
linkedin_id = db.Column(db.String)
date_registered = db.Column(db.DateTime, default=timestamp)
last_validation_date = db.Column(db.DateTime, default=timestamp)
accepted_licenses = db.relationship('License', secondary=users_licenses_table)
def create(self):...
"""docstring"""
db.session.add(self)
db.session.commit()
def save(self):...
db.session.commit()
def get_by_id(self, user_id: int):...
"""docstring"""
return User.query.get(user_id)
