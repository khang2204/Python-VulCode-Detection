def test_inactive(self):...
self.user.is_active = False
self.user.save()
meta = DEF_SHIBD_META.copy()
meta['SHIB_eppn'] = self.user.username.encode('utf-8')
response = self._get(meta)
self.assertEqual(response.status_code, 403)
self.assertEqual(User.objects.count(), 1)
