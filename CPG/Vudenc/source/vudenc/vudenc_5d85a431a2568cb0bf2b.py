import sys
import logging
from django.db import connection, DatabaseError
from reviewus.settings import DEBUG
logger = logging.getLogger(__name__)
instance = None
con = None
def __new__(cls):...
if DBConnection.instance is None:
DBConnection.instance = object.__new__(cls)
return DBConnection.instance
