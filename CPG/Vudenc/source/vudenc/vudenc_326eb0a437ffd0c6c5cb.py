def submit_background_work_chain(self, work_chain, parent_workunit_name=None):...
"""docstring"""
background_root_workunit = self.run_tracker.get_background_root_workunit()
if parent_workunit_name:
workunit_parent_ctx = self.run_tracker.new_workunit_under_parent(name=
    parent_workunit_name, labels=[WorkUnitLabel.MULTITOOL], parent=
    background_root_workunit)
workunit_parent = background_root_workunit
workunit_parent = workunit_parent_ctx.__enter__()
done_hook = None
done_hook = lambda : workunit_parent_ctx.__exit__(None, None, None)
self.run_tracker.background_worker_pool().submit_async_work_chain(work_chain,
    workunit_parent=workunit_parent, done_hook=done_hook)
