def __init__(self):...
self._job_status = defaultdict(functools.partial(defaultdict, str))
self._job_text = defaultdict(str)
self._job_error_text = defaultdict(str)
self._job_percent = defaultdict(int)
self._job_exitstatus = {}
self._stop_events = {}
self._latest_job_id = 0
