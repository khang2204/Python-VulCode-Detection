def cancel_node_jobs(self):...
cancel_finished = True
for n in self.nodes:
obj = n['node_object']
return cancel_finished
job = obj.job
if not job:
if job.can_cancel:
cancel_finished = False
job.cancel()
