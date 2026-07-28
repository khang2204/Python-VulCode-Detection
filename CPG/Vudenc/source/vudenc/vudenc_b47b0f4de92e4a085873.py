@staticmethod...
"""docstring"""
data = {}
if not report:
report = AnalysisController.get_report(task_id)['analysis']
procs = AnalysisController.behavior_get_processes(task_id, report)
for proc in procs['data']:
pid = proc['pid']
return data
pname = proc['process_name']
pdetails = None
for p in report['behavior']['generic']:
if p['pid'] == pid:
if not pdetails:
pdetails = p
watchers = AnalysisController.behavior_get_watchers(task_id, pid=pid,
    report=report)
for category, events in watchers.iteritems():
if not data.has_key(category):
data[category] = {}
if not data[category].has_key(pid):
data[category][pname] = {'pid': pid, 'process_name': pname, 'events': {}}
for event in events:
if not data[category][pname]['events'].has_key(event):
data[category][pname]['events'][event] = []
for _event in pdetails['summary'][event]:
data[category][pname]['events'][event].append(_event)
