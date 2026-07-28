def enrollment_audience_check(self, request, course, user):...
audience = course.enrollment_audience
external = user.userprofile.is_external
EA = course.ENROLLMENT_AUDIENCE
if audience == EA.INTERNAL_USERS and external:
self.error_msg(_('This course is only for internal students.'))
if audience == EA.EXTERNAL_USERS and not external:
return False
self.error_msg(_('This course is only for external students.'))
return True
return False
