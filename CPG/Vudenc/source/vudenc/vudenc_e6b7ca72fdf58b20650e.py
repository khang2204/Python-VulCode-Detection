@staticmethod...
files = request.FILES.getlist('files[]')
data = []
if files:
for f in files:
body = json.loads(request.body)
data.append({'name': f.name, 'data': f.file})
submit_id = submit_manager.pre(submit_type='files', data=data)
submit_type = body['type']
return redirect('submission/pre', submit_id=submit_id)
if submit_type != 'strings':
return json_error_response('type not "strings"')
submit_id = submit_manager.pre(submit_type=submit_type, data=body['data'].
    split('\n'))
return JsonResponse({'status': True, 'submit_id': submit_id}, encoder=
    JsonSerialize)
