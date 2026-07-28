def retrieve(self, request, pk=None, project_pk=None):...
get_and_check_project(request, project_pk)
task = self.queryset.get(pk=pk, project=project_pk)
serializer = TaskSerializer(task)
return Response(serializer.data)
