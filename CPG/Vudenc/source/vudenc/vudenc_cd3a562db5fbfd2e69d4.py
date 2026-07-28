import logging
import traceback
from ..anagonda.context.autocomplete import AutoComplete
from commands.base import Command
"""Run GoCode
    """
def __init__(self, callback, uid, vid, code, path, offset, go_env):...
self.vid = vid
self.path = path
self.code = code
self.path = path
self.offset = offset
self.go_env = go_env
super(Gocode, self).__init__(callback, uid)
def run(self):...
"""docstring"""
self.callback({'success': True, 'completions': comps, 'uid': self.uid,
    'vid': self.vid})
logging.error(error)
logging.debug(traceback.format_exc())
self.callback({'success': False, 'error': str(error), 'uid': self.uid,
    'vid': self.vid})
