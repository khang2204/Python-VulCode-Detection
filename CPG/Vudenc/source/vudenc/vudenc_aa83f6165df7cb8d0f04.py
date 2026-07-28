def __init__(self, data):...
"""docstring"""
logging.info('TaskDetails(%s)', data)
if not isinstance(data, dict):
self.bot_id = data['bot_id']
self.command = data['command'] or []
self.inputs_ref = data['inputs_ref']
self.extra_args = data['extra_args']
self.env = {k.encode('utf-8'): v.encode('utf-8') for k, v in data['env'].
    iteritems()}
self.grace_period = data['grace_period']
self.hard_timeout = data['hard_timeout']
self.io_timeout = data['io_timeout']
self.task_id = data['task_id']
