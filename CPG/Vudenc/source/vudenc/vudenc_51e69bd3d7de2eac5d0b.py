@api_post...
submit_id = body.pop('submit_id', None)
submit_manager.submit(submit_id=submit_id, config=body)
return JsonResponse({'status': True, 'submit_id': submit_id}, encoder=
    JsonSerialize)
