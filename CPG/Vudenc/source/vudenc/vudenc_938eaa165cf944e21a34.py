def has_permission(self, request, view):...
if not view.is_course_staff:
module = view.module
return True
return self.has_object_permission(request, view, module)
