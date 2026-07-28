def test_nonascii(self):...
meta = DEF_SHIBD_META.copy()
meta['SHIB_eppn'] = self.user.username.encode('utf-8')
meta['SHIB_sn'] = 'Meikäläinen'
response = self._get(meta)
self.assertEqual(response.status_code, 302)
self.assertEqual(User.objects.count(), 1)
user = User.objects.first()
self.assertEqual(user.email, 'teemu.teekkari@aalto.fi')
self.assertEqual(user.first_name, 'Matti')
self.assertEqual(user.last_name, 'Meikäläinen')
self.assertEqual(user.userprofile.student_id, '000')
