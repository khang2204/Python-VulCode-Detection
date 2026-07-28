from django.conf import settings
from django.contrib import messages
from django.core.exceptions import MultipleObjectsReturned, PermissionDenied
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.views.static import serve
from authorization.permissions import ACCESS
from course.models import CourseModule
from course.viewbase import CourseInstanceBaseView, EnrollableViewMixin
from lib.remote_page import RemotePageNotFound, request_for_response
from lib.viewbase import BaseRedirectMixin, BaseView
from .models import LearningObject, LearningObjectDisplay
from .protocol.exercise_page import ExercisePage
from .submission_models import SubmittedFile, Submission
from .viewbase import ExerciseBaseView, SubmissionBaseView, SubmissionMixin, ExerciseModelBaseView, ExerciseTemplateBaseView
from .exercisecollection_models import ExerciseCollection
from .exercise_summary import UserExerciseSummary
from django.urls import reverse
template_name = 'exercise/toc.html'
template_name = 'exercise/results.html'
ajax_template_name = 'exercise/_exercise_info.html'
def get_common_objects(self):...
super().get_common_objects()
self.get_summary_submissions()
template_name = 'exercise/exercise.html'
ajax_template_name = 'exercise/exercise_plain.html'
post_url_name = 'exercise'
access_mode = ACCESS.STUDENT
@method_decorator(csrf_exempt)...
return super().dispatch(request, *args, **kwargs)
