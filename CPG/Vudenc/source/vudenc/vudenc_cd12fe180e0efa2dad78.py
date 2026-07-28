from __future__ import absolute_import
import datetime
from .config import get_config_file_paths
from .util import *
GOALS_CONFIG_FILE_PATH = get_config_file_paths()['GOALS_CONFIG_FILE_PATH']
GOALS_CONFIG_FOLDER_PATH = get_folder_path_from_file_path(
    GOALS_CONFIG_FILE_PATH)
def strike(text):...
"""docstring"""
return u'̶'.join(text) + u'̶'
