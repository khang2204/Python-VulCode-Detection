from django.db.models.signals import post_save, post_delete, m2m_changed
from django.utils import timezone
from lib.cache import CachedAbstract
from ..models import StudentGroup, Enrollment, CourseInstance, Course
from ..renders import render_group_info
KEY_PREFIX = 'topmenu'
def __init__(self, user):...
self.user = user
super().__init__(user)
def _generate_data(self, user, data=None):...
profile = user.userprofile if user and user.is_authenticated() else None
return {'courses': self._generate_courses(profile), 'groups': self.
    _generate_groups(profile)}
