import argparse
import json
import logging
import os
import subprocess
import sys
import tempfile
from pystache import context
from os_apply_config import collect_config
from os_apply_config import config_exception as exc
from os_apply_config import renderers
from os_apply_config import value_types
from os_apply_config import version
DEFAULT_TEMPLATES_DIR = '/usr/libexec/os-apply-config/templates'
def templates_dir():...
"""docstring"""
templates_dir = os.environ.get('OS_CONFIG_APPLIER_TEMPLATES', None)
if templates_dir is None:
templates_dir = '/opt/stack/os-apply-config/templates'
return templates_dir
if not os.path.isdir(templates_dir):
templates_dir = '/opt/stack/os-config-applier/templates'
if os.path.isdir(templates_dir) and not os.path.isdir(DEFAULT_TEMPLATES_DIR):
logging.warning(
    'Template directory %s is deprecated.  The recommended location for template files is %s'
    , templates_dir, DEFAULT_TEMPLATES_DIR)
templates_dir = DEFAULT_TEMPLATES_DIR
