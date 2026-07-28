def unpack_history_info(item):...
"""docstring"""
lst = item['stage_log']
if lst:
if item['script_log']:
lines = lst.split('\r\n')
logging.error(T('Invalid stage logging in history for %s') + ' (\\r\\n)',
    unicoder(item['name']))
lst = [None for x in STAGES]
item['script_log'] = ''
if 'action_line' not in item:
logging.debug('Lines: %s', lst)
for line in lines:
item['action_line'] = ''
return item
lines = []
stage = {}
item['stage_log'] = [x for x in lst if x is not None]
key, logs = line.split(':::')
logging.debug('Missing key:::logs "%s"', line)
stage['name'] = key
key = line
stage['actions'] = []
logs = ''
logs = logs.split(';')
logging.error(T('Invalid stage logging in history for %s') + ' (;)',
    unicoder(item['name']))
for log in logs:
logging.debug('Logs: %s', logs)
stage['actions'].append(log)
lst[STAGES[key]] = stage
lst.append(stage)
logs = []
