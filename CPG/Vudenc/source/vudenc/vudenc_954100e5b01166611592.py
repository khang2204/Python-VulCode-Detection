from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from authorization.permissions import ACCESS, Permission, MessageMixin, ObjectVisibleBasePermission, FilterBackend
from exercise.cache.points import CachedPoints
from userprofile.models import UserProfile
from .models import CourseModule, CourseInstance
message = _('Permission denied by course visibility')
model = CourseInstance
obj_var = 'instance'
def is_object_visible(self, request, view, course):...
"""docstring"""
if view.is_course_staff:
return True
if not course.visible_to_students:
self.error_msg(_('The resource is not currently visible.'))
user = request.user
return False
show_for = course.view_content_to
VA = course.VIEW_ACCESS
if show_for != VA.PUBLIC:
if not user.is_authenticated():
return True
self.error_msg(_('This course is not open for public.'))
if view.get_access_mode() == ACCESS.ENROLL:
return False
return self.enrollment_audience_check(request, course, user)
if show_for == VA.ENROLLED:
if not course.is_student(user):
if show_for == VA.ENROLLMENT_AUDIENCE:
self.error_msg(_('Only enrolled students shall pass.'))
return self.enrollment_audience_check(request, course, user)
return False
