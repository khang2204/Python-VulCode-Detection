def mocked_resource(self, resource_class, mock_validate=True,...
mocked = resource_class(nsx_client.NSX3Client(self.mock_nsx_clustered_api(
    session_response=session_response), nsx_api_managers=[NSX_MANAGER],
    max_attempts=NSX_MAX_ATTEMPTS), nsxlib_config=get_default_nsxlib_config
    (), nsxlib=self.nsxlib)
if mock_validate:
mock.patch.object(mocked.client, '_validate_result').start()
return mocked
