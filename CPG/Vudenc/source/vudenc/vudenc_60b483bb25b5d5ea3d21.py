@staticmethod...
if not task_id:
if not report:
report = AnalysisController.get_report(task_id)['analysis']
data = {'data': [], 'status': True}
for process in report.get('behavior', {}).get('generic', []):
data['data'].append({'process_name': process['process_name'], 'pid':
    process['pid']})
data['data'] = sorted(data['data'], key=lambda k: k['process_name'])
return data
