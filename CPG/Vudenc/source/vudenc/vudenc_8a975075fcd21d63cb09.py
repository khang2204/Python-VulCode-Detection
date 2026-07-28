from datetime import datetime, timedelta
import pytz
from constance.admin import Config, ConstanceAdmin, ConstanceForm
from cryptography.fernet import Fernet
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils.safestring import mark_safe
from django_celery_beat.admin import PeriodicTaskAdmin, PeriodicTaskForm
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from dashboard.internet_nl_dashboard.models import Account, DashboardUser, UploadLog, UrlList
fieldsets = PeriodicTaskAdmin.fieldsets
"""
    Interval schedule does not support due_ or something. Which is absolutely terrible and vague.
    I can't understand why there is not an is_due() for each type of schedule. This makes it very hazy
    when something will run.

    Because of this, we'll move to the horrifically designed absolute nightmare format Crontab.
    Crontab would be half-great if the parameters where named.

    Get your crontab guru going, this is the only way you'll understand what you're doing.
    https://crontab.guru/#0_21_*_*_*
    """
def clean(self):...
print('cleaning')
cleaned_data = super(PeriodicTaskForm, self).clean()
return cleaned_data
