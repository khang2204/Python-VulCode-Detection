def mock_import_repository_task(*args, **kwargs):...
resp = requests.Response()
resp.status_code = 200
resp._content_consumed = True
return resp
