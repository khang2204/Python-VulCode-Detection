from django.db.models.signals import post_save, post_delete
from lib.cache import CachedAbstract
from .models import Notification
KEY_PREFIX = 'notifications'
def __init__(self, user):...
super().__init__(user)
def _generate_data(self, user, data=None):...
if not user or not user.is_authenticated():
return {'count': 0, 'notifications': []}
def notification_entry(n):...
exercise = n.submission.exercise if n.submission else None
return {'id': n.id, 'submission_id': n.submission.id if n.submission else 0,
    'name': '{} {}, {}'.format(n.course_instance.course.code, str(exercise.
    parent) if exercise and exercise.parent else n.course_instance.
    instance_name, str(exercise) if exercise else n.subject), 'link': n.
    get_display_url()}
