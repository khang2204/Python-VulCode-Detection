@contextmanager...
"""docstring"""
self._set_target_root_count_in_runtracker()
yield
self.run_tracker.pantsd_stats.set_scheduler_metrics(self._scheduler.metrics())
self._set_affected_target_count_in_runtracker()
