def _cmd_sleep(self, sleep_streak, quarantined):...
out = {'cmd': 'sleep', 'duration': task_scheduler.exponential_backoff(
    sleep_streak), 'quarantined': quarantined}
self.send_response(out)
