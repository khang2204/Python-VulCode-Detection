@staticmethod...
if not task_id or not watcher or not pid:
if not report:
report = AnalysisController.get_report(task_id)['analysis']
behavior_generic = report['behavior']['generic']
process = [z for z in behavior_generic if z['pid'] == pid]
if not process:
process = process[0]
summary = process['summary']
if watcher not in summary:
if offset:
summary[watcher] = summary[watcher][offset:]
if limit:
summary[watcher] = summary[watcher][:limit]
return summary[watcher]
