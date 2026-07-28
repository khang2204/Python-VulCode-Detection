def list(self, request, project_pk=None):...
get_and_check_project(request, project_pk)
tasks = self.queryset.filter(project=project_pk)
tasks = filters.OrderingFilter().filter_queryset(self.request, tasks, self)
serializer = TaskSerializer(tasks, many=True)
return Response(serializer.data)
