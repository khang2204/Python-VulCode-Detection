import os
import time
from cauldron.render import texts as render_texts
from cauldron.session.buffering import RedirectBuffer
from cauldron.session.caching import SharedCache
"""
    The display management class for each step in a project. These class
    instances are exposed to Cauldron users, which provide the functionality
    for adding various element types to the display.
    """
def __init__(self, step=None):...
self.step = step
self.body = []
self.css = []
self.data = SharedCache()
self.files = SharedCache()
self.title = self.definition.get('title')
self.subtitle = self.definition.get('subtitle')
self.summary = self.definition.get('summary')
self.library_includes = []
self.stdout_interceptor = None
self.stderr_interceptor = None
self._last_update_time = 0
@property...
"""docstring"""
stdout = self.stdout_interceptor
stderr = self.stderr_interceptor
return max([self._last_update_time, stdout.last_write_time if stdout else 0,
    stderr.last_write_time if stderr else 0])
