def get(self, request, pk=None, project_pk=None):...
"""docstring"""
task = self.get_and_check_task(request, pk, project_pk, annotate={
    'orthophoto_area': Envelope(Cast('orthophoto', GeometryField()))})
json = get_tile_json(task.name, [
    '/api/projects/{}/tasks/{}/tiles/{{z}}/{{x}}/{{y}}.png'.format(task.
    project.id, task.id)], task.orthophoto_area.extent)
return Response(json)
