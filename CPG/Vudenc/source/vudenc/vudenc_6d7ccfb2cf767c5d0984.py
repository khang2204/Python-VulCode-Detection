import copy
import logging
import os
import sflock
from cuckoo.common.config import emit_options
from cuckoo.common.exceptions import CuckooOperationalError
from cuckoo.common.files import Folders, Files, Storage
from cuckoo.common.utils import validate_url, validate_hash
from cuckoo.common.virustotal import VirusTotalAPI
from cuckoo.core.database import Database
log = logging.getLogger(__name__)
db = Database()
def _handle_string(self, submit, tmppath, line):...
if not line:
return
if validate_hash(line):
if validate_url(line):
filedata = VirusTotalAPI().hash_fetch(line)
submit['errors'].append('Error retrieving file hash: %s' % e)
filepath = Files.create(tmppath, line, filedata)
submit['data'].append({'type': 'url', 'data': line})
submit['errors'].append("'%s' was neither a valid hash or url" % line)
return
submit['data'].append({'type': 'file', 'data': filepath})
return
def pre(self, submit_type, data):...
return
"""docstring"""
if submit_type not in ('strings', 'files'):
log.error("Bad parameter '%s' for submit_type", submit_type)
path_tmp = Folders.create_temp()
return False
submit_data = {'data': [], 'errors': []}
if submit_type == 'strings':
for line in data:
if submit_type == 'files':
self._handle_string(submit_data, path_tmp, line)
for entry in data:
return Database().add_submit(path_tmp, submit_type, submit_data)
filename = Storage.get_filename_from_path(entry['name'])
filepath = Files.create(path_tmp, filename, entry['data'])
submit_data['data'].append({'type': 'file', 'data': filepath})
