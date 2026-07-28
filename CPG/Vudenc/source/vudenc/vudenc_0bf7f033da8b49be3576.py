def _set_target_root_count_in_runtracker(self):...
"""docstring"""
target_count = len(self._target_roots)
self.run_tracker.pantsd_stats.set_target_root_size(target_count)
return target_count
