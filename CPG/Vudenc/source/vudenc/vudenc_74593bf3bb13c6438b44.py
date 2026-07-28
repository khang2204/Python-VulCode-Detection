def clean_bug_form(request):...
"""docstring"""
data = {}
data['bugs'] = request.GET.get('bug_id', '').split(',')
return None, 'Please specify only integers for bugs, caseruns(using comma to seperate IDs), and bug_system. (DEBUG INFO: %s)' % str(
    e)
data['bug_system_id'] = int(request.GET.get('bug_system_id', 1))
data['runs'] = map(int, request.GET.get('case_runs', '').split(','))
if request.GET.get('a') not in ('add', 'remove'):
return None, 'Actions only allow "add" and "remove".'
data['action'] = request.GET.get('a')
data['bz_external_track'] = True if request.GET.get('bz_external_track', False
    ) else False
return data, ''
