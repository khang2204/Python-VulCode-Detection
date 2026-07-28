def _new_client_for(*args, **kwargs):...
sub_client = new_client_for(*args, **kwargs)
if mock_validate:
mock.patch.object(sub_client, '_validate_result').start()
return sub_client
