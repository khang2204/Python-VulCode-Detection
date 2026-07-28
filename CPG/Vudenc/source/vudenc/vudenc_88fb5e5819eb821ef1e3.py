from datetime import datetime
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from mdta.celery_module import app
from mdta.apps.projects.models import Project
from mdta.apps.testcases.models import TestCaseResults
from mdta.apps.testcases.utils import create_routing_test_suite, add_testsuite_to_project, remove_section_from_testsuite, add_section_to_testsuite, add_testcase_to_section
from mdta.apps.testcases.testrail import APIClient
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
