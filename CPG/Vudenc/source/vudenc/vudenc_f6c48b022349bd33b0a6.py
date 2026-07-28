"""
Shared functions for plan/case/run.

Most of these functions are use for Ajax.
"""
import datetime
import sys
import json
from distutils.util import strtobool
from django import http
from django.db.models import Q, Count
from django.contrib.auth.models import User
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.apps import apps
from django.forms import ValidationError
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST
from tcms.signals import POST_UPDATE_SIGNAL
from tcms.management.models import Component, Build, Version
from tcms.management.models import Priority
from tcms.management.models import Tag
from tcms.management.models import EnvGroup, EnvProperty, EnvValue
from tcms.testcases.models import TestCase, Bug
from tcms.testcases.models import Category
from tcms.testcases.models import TestCaseStatus, TestCaseTag
from tcms.testcases.views import plan_from_request_or_none
from tcms.testplans.models import TestPlan, TestCasePlan, TestPlanTag
from tcms.testruns.models import TestRun, TestCaseRun, TestCaseRunStatus, TestRunTag
from tcms.core.helpers.comments import add_comment
from tcms.core.utils.validations import validate_bug_id
def check_permission(request, ctype):...
perm = '%s.change_%s' % tuple(ctype.split('.'))
if request.user.has_perm(perm):
return True
return False
