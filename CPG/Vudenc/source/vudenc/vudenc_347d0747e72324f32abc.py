"""The base class of the TornadoResource classes in the api module."""
from abc import ABCMeta, abstractmethod
from collections import OrderedDict
from time import localtime
from passlib.hash import bcrypt_sha256
from restless.tnd import TornadoResource
import restless.exceptions as exc
from sqlalchemy import text, func
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.functions import count
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound
import tornado.web
from dokomoforms.api.serializer import ModelJSONSerializer
from dokomoforms.handlers.util import BaseHandler, BaseAPIHandler
from dokomoforms.models import SurveyCreator, Email
from dokomoforms.models.util import column_search, get_fields_subset
from dokomoforms.exc import DokomoError
"""Set up the basics for the model resource.

    BaseResource does some basic configuration for the restless resources.
    - sets the base request handler class which is used by the resources
    - providing reference to the ORM session via request handler
    - inserting a serializer for dokomo Models
    - setting up authentication
    """
_request_handler_base_ = BaseAPIHandler
serializer = ModelJSONSerializer()
@property...
"""docstring"""
@property...
"""docstring"""
@property...
"""docstring"""
@property...
"""docstring"""
return self.r_handler.session
