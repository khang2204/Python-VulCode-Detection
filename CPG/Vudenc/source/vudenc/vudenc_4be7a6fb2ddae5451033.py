def run(self, job_id):...
"""docstring"""
self.variable_manager.extra_vars = {'job_id': job_id}
self.pbex.run()
return self.pbex._tqm._stats
