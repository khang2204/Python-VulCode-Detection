@require_POST...
"""docstring"""
data = request.POST.copy()
comment = data.get('comment', None)
if not comment:
return say_no('Comments needed')
run_ids = [i for i in data.get('run', '').split(',') if i]
if not run_ids:
return say_no('No runs selected.')
runs = TestCaseRun.objects.filter(pk__in=run_ids).only('pk')
if not runs:
return say_no('No caserun found.')
add_comment(runs, comment, request.user)
return say_yes()
