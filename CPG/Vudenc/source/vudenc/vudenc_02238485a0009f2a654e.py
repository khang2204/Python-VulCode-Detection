def new_mocked_client(self, client_class, mock_validate=True,...
client = client_class(mock_cluster or self.mock_nsx_clustered_api(
    session_response=session_response), **kwargs)
if mock_validate:
mock.patch.object(client, '_validate_result').start()
new_client_for = client.new_client_for
def _new_client_for(*args, **kwargs):...
sub_client = new_client_for(*args, **kwargs)
if mock_validate:
mock.patch.object(sub_client, '_validate_result').start()
return sub_client
