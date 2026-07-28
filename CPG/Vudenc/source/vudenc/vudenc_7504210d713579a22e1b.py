def run(self):...
"""docstring"""
self.callback({'success': True, 'completions': comps, 'uid': self.uid,
    'vid': self.vid})
logging.error(error)
logging.debug(traceback.format_exc())
self.callback({'success': False, 'error': str(error), 'uid': self.uid,
    'vid': self.vid})
