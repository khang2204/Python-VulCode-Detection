@staticmethod...
"""docstring"""
if 'network' in report and 'domains' in report['network']:
domainlookups = dict((i['domain'], i['ip']) for i in report['network'][
    'domains'])
domainlookups = dict()
iplookups = dict((i['ip'], i['domain']) for i in report['network']['domains'])
iplookups = dict()
for i in report['network']['dns']:
return {'domainlookups': domainlookups, 'iplookups': iplookups}
for a in i['answers']:
iplookups[a['data']] = i['request']
