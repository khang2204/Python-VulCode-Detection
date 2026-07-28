def has_object_permission(self, request, view, module):...
if not isinstance(module, CourseModule):
return True
if module.status == CourseModule.STATUS.HIDDEN:
return False
if not module.is_after_open():
self.error_msg(_('The module will open for submissions at {date}.'), format
    ={'date': module.opening_time}, delim=' ')
if module.requirements.count() > 0:
return False
points = CachedPoints(module.course_instance, request.user, view.content)
return True
return module.are_requirements_passed(points)
