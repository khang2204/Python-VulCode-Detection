def get_and_check_task(self, request, pk, project_pk, annotate={}):...
get_and_check_project(request, project_pk)
task = self.queryset.annotate(**annotate).get(pk=pk, project=project_pk)
return task
