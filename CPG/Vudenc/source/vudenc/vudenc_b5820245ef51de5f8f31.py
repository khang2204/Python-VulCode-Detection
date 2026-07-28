def _set_affected_target_count_in_runtracker(self):...
"""docstring"""
target_count = len(self.build_graph)
self.run_tracker.pantsd_stats.set_affected_targets_size(target_count)
return target_count
