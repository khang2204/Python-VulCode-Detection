def update_bugs_to_caseruns(request):...
"""docstring"""
data, error = clean_bug_form(request)
if error:
return say_no(error)
runs = TestCaseRun.objects.filter(pk__in=data['runs'])
bug_system_id = data['bug_system_id']
bug_ids = data['bugs']
validate_bug_id(bug_ids, bug_system_id)
return say_no(str(e))
bz_external_track = data['bz_external_track']
action = data['action']
if action == 'add':
return say_no(str(e))
return say_yes()
for run in runs:
bugs = Bug.objects.filter(bug_id__in=bug_ids)
for bug_id in bug_ids:
for run in runs:
run.add_bug(bug_id=bug_id, bug_system_id=bug_system_id, bz_external_track=
    bz_external_track)
for bug in bugs:
if bug.case_run_id == run.pk:
run.remove_bug(bug.bug_id, run.pk)
