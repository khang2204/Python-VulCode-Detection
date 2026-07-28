def filter_queryset(self, request, queryset, view):...
user = request.user
if issubclass(queryset.model, UserProfile
queryset = queryset.filter(user_id=user.id)
return queryset
