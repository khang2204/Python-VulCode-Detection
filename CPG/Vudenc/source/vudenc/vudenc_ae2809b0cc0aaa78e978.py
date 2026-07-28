import sys
import os
import logging
import pdb
import urllib2
import json
import ijson
from dbnav.writer import Writer
from dbnav import logger as log
from dbnav.jsonable import from_json
COMMANDS = {'dbdiff': 'differ', 'dbexec': 'executer', 'dbexport':
    'exporter', 'dbgraph': 'grapher', 'dbnav': 'navigator'}
def __init__(self, options=None):...
self.options = options
def write(self):...
sys.stdout.write(Writer.write(self.run()))
log.logger.exception(e)
return 0
return -1
