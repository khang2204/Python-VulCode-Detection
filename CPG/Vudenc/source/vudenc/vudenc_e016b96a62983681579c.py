def remove_history(self, jobs=None):...
"""docstring"""
if jobs is None:
self.remove_completed()
if not isinstance(jobs, list):
self.save()
jobs = [jobs]
for job in jobs:
self.execute('DELETE FROM history WHERE nzo_id=?', (job,))
logging.info('Removing job %s from history', job)
