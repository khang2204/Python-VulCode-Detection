"""
Test core utility functions.
"""
import mock
from unittest import skip
from ddt import ddt, data, unpack
from django.conf import settings
from django.contrib.sites.models import Site
from django.core import mail
from django.test import TestCase
from core.common.utils import send_email, get_onboarding_percentage
from core.common import onboarding
from core.common.utils import get_onboarding_setting, ONBOARDING_STEPS_DEFAULT_TEMPLATE, get_onboarding_status_with_settings
"""
    Test auxiliary functions.
    """
def test_send_email(self):...
"""docstring"""
send_email(context_data={'milestone': 'first', 'students_number': 2,
    'course_title': 'Test Course', 'lesson_title': 'Test Lesson',
    'current_site': Site.objects.get_current(), 'course_id': 1,
    'unit_lesson_id': 1, 'courselet_pk': 1}, from_email=settings.EMAIL_FROM,
    to_email=['test@example.com'], template_subject=
    'ct/email/milestone_ortc_notify_subject', template_text=
    'ct/email/milestone_ortc_notify_text')
self.assertEqual(len(mail.outbox), 1)
@mock.patch('core.common.utils.c_onboarding_status')...
_mock = mock.return_value
_mock.find_one.return_value = steps
self.assertEqual(get_onboarding_percentage(1), result)
@mock.patch('core.common.utils.c_onboarding_status')...
self.assertEqual(get_onboarding_setting(setting_name), value)
@skip...
def mocked_setting(setting_name):...
data = {onboarding.INTRODUCTION_INTRO: {'html': '<p>instructor_intro</p>',
    'description': 'instructor_intro desc', 'title': 'instructor_intro'},
    onboarding.CREATE_COURSE: {'html': '<p>create_course</p>',
    'description': 'create_course desc', 'title': 'create_course'},
    onboarding.CREATE_COURSELET: {'html': '<p>create_courselet</p>',
    'description': 'create_courselet desc', 'title': 'create_courselet'},
    onboarding.NEXT_STEPS: {'html': '<p>next_steps</p>', 'description':
    'next_steps desc', 'title': 'next_steps'}, onboarding.INVITE_SOMEBODY:
    {'html': '<p>invite_somebody</p>', 'description':
    'invite_somebody desc', 'title': 'invite_somebody'}, onboarding.
    CREATE_THREAD: {'html': '<p>create_thread</p>', 'description':
    'create_thread desc', 'title': 'create_thread'}, onboarding.
    VIEW_INTRODUCTION: {'html': '<p>view_introduction</p>', 'description':
    'view_introduction desc', 'title': 'view_introduction'}, onboarding.
    PREVIEW_COURSELET: {'html': '<p>preview_courselet</p>', 'description':
    'preview_courselet desc', 'title': 'preview_courselet'}}
return data[setting_name]
