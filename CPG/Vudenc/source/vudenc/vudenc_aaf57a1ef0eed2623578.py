def get(self, request, *args, **kwargs):...
bytedata = f.read()
if request.GET.get('download', False):
response = HttpResponse(bytedata, content_type='application/octet-stream')
if self.file.is_passed():
response['Content-Disposition'] = 'attachment; filename="{}"'.format(self.
    file.filename)
return HttpResponse(bytedata, content_type=self.file.get_mime())
return HttpResponse(bytedata.decode('utf-8', 'ignore'), content_type=
    'text/plain; charset="UTF-8"')
return response
