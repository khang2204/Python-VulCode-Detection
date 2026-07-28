@staticmethod...
if not task_id or not pid:
if not report:
report = AnalysisController.get_report(task_id)['analysis']
behavior_generic = report['behavior']['generic']
process = [z for z in behavior_generic if z['pid'] == pid]
if not process:
process = process[0]
data = {}
for category, watchers in AnalysisController.behavioral_mapping().iteritems():
for watcher in watchers:
return data
if watcher in process['summary']:
if category not in data:
data[category] = [watcher]
data[category].append(watcher)
