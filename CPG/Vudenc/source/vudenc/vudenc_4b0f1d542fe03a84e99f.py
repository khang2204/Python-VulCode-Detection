from cachetools import TTLCache, cached
from flask import current_app
from functools import reduce
import dateutil.parser
import datetime
from server import db
from server.models.dtos.user_dto import UserDTO, UserOSMDTO, UserFilterDTO, UserSearchQuery, UserSearchDTO, UserStatsDTO
from server.models.dtos.message_dto import MessageDTO
from server.models.postgis.message import Message
from server.models.postgis.task import TaskHistory
from server.models.postgis.user import User, UserRole, MappingLevel
from server.models.postgis.utils import NotFound
from server.services.users.osm_service import OSMService, OSMServiceError
from server.services.messaging.smtp_service import SMTPService
from server.services.messaging.template_service import get_template
user_filter_cache = TTLCache(maxsize=1024, ttl=600)
user_all_cache = TTLCache(maxsize=1024, ttl=600)
""" Custom Exception to notify callers an error occurred when in the User Service """
def __init__(self, message):...
if current_app:
current_app.logger.error(message)
@staticmethod...
user = User().get_by_id(user_id)
if user is None:
return user
