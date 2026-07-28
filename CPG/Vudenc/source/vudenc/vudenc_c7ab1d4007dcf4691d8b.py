def has_object_permission(self, request, view, obj):...
user = request.user
return not isinstance(obj, self.model
    ) or user.is_staff or user.is_superuser or self.is_object_visible(request,
    view, obj)
