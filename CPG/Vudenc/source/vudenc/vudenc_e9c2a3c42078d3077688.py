import json
from django import template
from django.db.models import Max, Min
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from course.models import CourseModule
from lib.errors import TagUsageError
from ..cache.content import CachedContent
from ..cache.points import CachedPoints
from ..exercise_summary import UserExerciseSummary
from ..models import LearningObjectDisplay, LearningObject, Submission, BaseExercise
register = template.Library()
def _prepare_now(context):...
if not 'now' in context:
context['now'] = timezone.now()
return context['now']
