@app.task...
"""docstring"""
project = get_object_or_404(Project, pk=project_id)
testcases = create_routing_test_suite(project=project)
tc_results = TestCaseResults.objects.filter(project=project)
if tc_results.count() > 2:
tc_latest = project.testcaseresults_set.latest('updated')
TestCaseResults.objects.create(project=project, results=testcases)
print(str(e))
msg = 'TestCases updated.'
if tc_latest.results == testcases:
if not call_from:
tc_latest.updated = datetime.now()
tc_earliest = project.testcaseresults_set.earliest('updated')
msg = push_testcases_to_testrail_celery(project.id)
return msg
tc_latest.save()
tc_earliest.results = testcases
tc_earliest.updated = datetime.now()
tc_earliest.save()
