def get(self, request, pk=None, project_pk=None, z='', x='', y=''):...
"""docstring"""
task = self.get_and_check_task(request, pk, project_pk)
tile_path = task.get_tile_path(z, x, y)
if os.path.isfile(tile_path):
tile = open(tile_path, 'rb')
return HttpResponse(FileWrapper(tile), content_type='image/png')
