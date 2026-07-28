def test_edit_redirect(self):...
dgpk = self.objects.dg.pk
dspk = str(self.objects.ds.pk)
gtpk = str(self.objects.gt.pk)
data = {'name': ['Changed Name'], 'group_type': [gtpk], 'downloaded_by': [
    str(User.objects.get(username='Karyn').pk)], 'downloaded_at': [
    '08/20/2017'], 'data_source': [dspk]}
response = self.client.post(f'/datagroup/edit/{dgpk}/', data=data)
self.assertEqual(response.status_code, 302,
    'User is redirected to detail page.')
self.assertEqual(response.url, f'/datagroup/{dgpk}/',
    'Should go to detail page.')
