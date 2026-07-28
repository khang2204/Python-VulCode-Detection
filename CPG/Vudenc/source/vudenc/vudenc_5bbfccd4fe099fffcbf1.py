@staticmethod...
report = AnalysisController._get_report(task_id)
if not report:
data = {'analysis': report}
dnsinfo = AnalysisController._get_dnsinfo(report)
data.update(dnsinfo)
return data
