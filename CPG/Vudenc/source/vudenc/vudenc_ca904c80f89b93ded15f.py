from copy import deepcopy
from django.db.models.signals import post_save, post_delete, m2m_changed
from django.utils import timezone
from lib.cache import CachedAbstract
from notification.models import Notification
from ..models import LearningObject, Submission
from .hierarchy import ContentMixin
KEY_PREFIX = 'points'
def __init__(self, course_instance, user, content):...
self.content = content
self.instance = course_instance
self.user = user
super().__init__(course_instance, user)
def _needs_generation(self, data):...
return data is None or data['created'] < self.content.created()
