def create(self, request, project_pk=None):...
project = get_and_check_project(request, project_pk, ('change_project',))
files = [file for filesList in map(lambda key: request.FILES.getlist(key),
    [keys for keys in request.FILES]) for file in filesList]
task = models.Task.create_from_images(files, project)
if task is not None:
return Response({'id': task.id}, status=status.HTTP_201_CREATED)
