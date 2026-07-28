import socket
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
import json
from mdta.apps.projects.models import Project, Module, TestRailInstance, TestRailConfiguration
from mdta.apps.projects.utils import context_project_dashboard
from mdta.apps.testcases.models import TestCaseResults
from mdta.apps.testcases.tasks import create_testcases_celery, push_testcases_to_testrail_celery
from mdta.apps.users.views import user_is_superuser, user_is_staff
from .utils import context_testcases, get_projects_from_testrail, create_routing_test_suite
from .forms import TestrailConfigurationForm
from mdta.apps.testcases.testrail import APIClient
from mdta.celery_module import app as celery_app
@login_required...
if request.user.humanresource.project:
project = request.user.humanresource.project
testcases = []
testcases = project.testcaseresults_set.latest('updated').results
testcases = []
context = {'project': project, 'testcases': testcases}
project = None
if project:
return render(request, 'testcases/tcs_project.html', context)
return redirect('graphs:projects_for_selection')
