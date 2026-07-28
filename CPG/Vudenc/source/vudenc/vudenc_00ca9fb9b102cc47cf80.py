def get_request_written_data(_=None):...
written_data = request.getWrittenData()
if written_data:
return get_str(written_data)
