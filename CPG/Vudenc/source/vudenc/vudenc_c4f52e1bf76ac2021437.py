def get(self, request, pk=None, project_pk=None, asset=''):...
"""docstring"""
task = self.get_and_check_task(request, pk, project_pk)
allowed_assets = {'all': 'all.zip', 'geotiff': os.path.join(
    'odm_orthophoto', 'odm_orthophoto.tif'), 'las': os.path.join(
    'odm_georeferencing', 'odm_georeferenced_model.ply.las'), 'ply': os.
    path.join('odm_georeferencing', 'odm_georeferenced_model.ply'), 'csv':
    os.path.join('odm_georeferencing', 'odm_georeferenced_model.csv')}
if asset in allowed_assets:
asset_path = task.assets_path(allowed_assets[asset])
if not os.path.exists(asset_path):
asset_filename = os.path.basename(asset_path)
file = open(asset_path, 'rb')
response = HttpResponse(FileWrapper(file), content_type=mimetypes.
    guess_type(asset_filename)[0] or 'application/zip')
response['Content-Disposition'] = 'attachment; filename={}'.format(
    asset_filename)
return response
