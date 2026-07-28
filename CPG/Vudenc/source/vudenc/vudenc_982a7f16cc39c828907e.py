import sys
import logging
import sqlalchemy as sa
from . import filters
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from sqlalchemy.orm.properties import SynonymProperty
from ..base import BaseInterface
from ..group import GroupByDateYear, GroupByDateMonth, GroupByCol
from ..mixins import FileColumn, ImageColumn
from ...filemanager import FileManager, ImageManager
from ..._compat import as_unicode
from ...const import LOGMSG_ERR_DBI_ADD_GENERIC, LOGMSG_ERR_DBI_EDIT_GENERIC, LOGMSG_ERR_DBI_DEL_GENERIC, LOGMSG_WAR_DBI_ADD_INTEGRITY, LOGMSG_WAR_DBI_EDIT_INTEGRITY, LOGMSG_WAR_DBI_DEL_INTEGRITY
log = logging.getLogger(__name__)
def _include_filters(obj):...
for key in filters.__all__:
if not hasattr(obj, key):
"""
    SQLAModel
    Implements SQLA support methods for views
    """
setattr(obj, key, getattr(filters, key))
session = None
filter_converter_class = filters.SQLAFilterConverter
def __init__(self, obj, session=None):...
_include_filters(self)
self.list_columns = dict()
self.list_properties = dict()
self.session = session
for prop in sa.orm.class_mapper(obj).iterate_properties:
if type(prop) != SynonymProperty:
for col_name in obj.__mapper__.columns.keys():
self.list_properties[prop.key] = prop
if col_name in self.list_properties:
super(SQLAInterface, self).__init__(obj)
self.list_columns[col_name] = obj.__mapper__.columns[col_name]
@property...
"""docstring"""
return self.obj.__name__
