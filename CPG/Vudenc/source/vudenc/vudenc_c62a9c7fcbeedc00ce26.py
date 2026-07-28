def is_object_visible(self, request, view, course_instance):...
if view.is_course_staff:
return True
if not course_instance.visible_to_students:
self.error_msg(_('The resource is not currently visible.'))
if course_instance.view_content_to != course_instance.VIEW_ACCESS.PUBLIC and not request.user.is_authenticated:
return False
self.error_msg(_('This course is not open for public.'))
return True
return False
