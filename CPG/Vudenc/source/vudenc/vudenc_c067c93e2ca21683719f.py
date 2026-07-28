@login_required...
dg = DataGroup.objects.get(pk=pk)
zip_file_name = f'{dg.fs_id}.zip'
zip_file = open(dg.get_zip_url(), 'rb')
response = HttpResponse(zip_file, content_type='application/zip')
response['Content-Disposition'] = 'attachment; filename=%s' % zip_file_name
return response
