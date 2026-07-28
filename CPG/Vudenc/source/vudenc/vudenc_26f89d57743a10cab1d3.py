@staticmethod...
"""docstring"""
if not task_id:
if not signatures:
signatures = AnalysisController.get_report(task_id)['signatures']
data = collections.OrderedDict()
for signature in signatures:
severity = signature['severity']
return data
if severity > 3:
severity = 3
if not data.has_key(severity):
data[severity] = []
data[severity].append(signature)
