def has_permission(self, request, view):...
access_mode = view.get_access_mode()
if access_mode == ACCESS.ANONYMOUS:
return True
if not request.user.is_authenticated():
return False
if access_mode >= ACCESS.SUPERUSER:
return request.user.is_superuser
if access_mode >= ACCESS.TEACHER:
if not view.is_teacher:
if access_mode >= ACCESS.ASSISTANT:
self.error_msg(_('Only course teachers shall pass.'))
return True
if not view.is_course_staff:
if access_mode == ACCESS.ENROLLED:
return False
self.error_msg(_('Only course staff shall pass.'))
if not view.is_course_staff and not view.is_student:
return False
self.error_msg(_('Only enrolled students shall pass.'))
return False
