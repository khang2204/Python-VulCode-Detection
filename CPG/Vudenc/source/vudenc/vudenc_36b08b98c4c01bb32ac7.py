def test_json_request(self):...
resp = mocks.MockRequestsResponse(200, jsonutils.dumps({'result': {'ok': 200}})
    )
api = self.new_mocked_client(client.JSONRESTClient, session_response=resp,
    url_prefix='api/v2/nat')
resp = api.create(body={'name': 'mgmt-egress'})
assert_json_call('post', api, 'https://1.2.3.4/api/v2/nat', data=jsonutils.
    dumps({'name': 'mgmt-egress'}))
self.assertEqual(resp, {'result': {'ok': 200}})
