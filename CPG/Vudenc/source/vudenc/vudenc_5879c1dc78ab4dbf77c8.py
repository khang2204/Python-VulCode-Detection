"""Versioned singleton entity with the global configuration."""
import logging
from google.appengine.ext import ndb
from gae_libs.model.versioned_model import VersionedModel
"""Singleton entity with the global configuration of the service.

  All changes are stored in the revision log.
  """
updated_ts = ndb.DateTimeProperty(indexed=False, auto_now=True)
updated_by = ndb.StringProperty(indexed=False)
@classmethod...
"""docstring"""
config_data = cls.GetVersion(version=version)
return config_data or cls() if version is None else config_data
