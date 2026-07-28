import logging
from django.contrib import admin
from django.contrib import messages
from checkcve.forms import CheckCVEForm, CheckCVEChangeForm
from checkcve.models import Checkcve, Software, WhiteList, Cve
from checkcve.utils import create_check_cve_task
logger = logging.getLogger(__name__)
form = CheckCVEForm
def check_cve(self, request, obj):...
errors = list()
test = True
for probe in obj:
if test:
probe.check_cve()
test = False
messages.add_message(request, messages.SUCCESS, 'Check CVE OK')
messages.add_message(request, messages.ERROR, 'Check CVE failed ! ' + str(
    errors))
logger.exception('Error in check_cve ' + str(self.actions))
actions = [check_cve]
errors.append(str(e))
def save_model(self, request, obj, form, change):...
create_check_cve_task(obj)
super().save_model(request, obj, form, change)
def get_form(self, request, obj=None, **kwargs):...
"""docstring"""
if obj is None:
return super(CheckCVEAdmin, self).get_form(request, obj, **kwargs)
return CheckCVEChangeForm
