def test_mask_password(self):...
pwds = 'my!pwd0#', 'some0therlong$pwd', 'pwd'
body = {'name_pwd': 'name1', 'password': pwds[0], 'some_list': {
    'name_password': 'name2', 'password': pwds[1]}, 'password': pwds[2]}
cl = client.RESTClient(None)
json_body = jsonutils.dumps(body)
masked_body = cl._mask_password(json_body)
for pwd in pwds:
json_body = json_body.replace('"' + pwd + '"', '"********"')
self.assertEqual(json_body, masked_body)
