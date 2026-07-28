@api_post...
submit_id = body.get('submit_id', 0)
password = body.get('password', None)
astree = body.get('astree', True)
data = submit_manager.get_files(submit_id=submit_id, password=password,
    astree=astree)
return JsonResponse({'status': True, 'data': data, 'defaults': defaults()},
    encoder=JsonSerialize)
