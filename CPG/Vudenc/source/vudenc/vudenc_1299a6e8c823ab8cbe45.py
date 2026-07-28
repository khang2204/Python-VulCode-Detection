def has_object_permission(self, request, view, obj):...
if not isinstance(obj, UserProfile):
return True
user = request.user
return user and (user.id is not None and user.id == obj.user_id or super().
    has_object_permission(request, view, obj))
