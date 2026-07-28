def update(self, request, pk=None, project_pk=None, partial=False):...
get_and_check_project(request, project_pk, ('change_project',))
task = self.queryset.get(pk=pk, project=project_pk)
serializer = TaskSerializer(task, data=request.data, partial=partial)
serializer.is_valid(raise_exception=True)
serializer.save()
scheduler.process_pending_tasks(background=True)
return Response(serializer.data)
