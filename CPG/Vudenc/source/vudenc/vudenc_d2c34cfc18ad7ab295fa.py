def test_valid_old(self):...
meta = DEF_SHIBD_META.copy()
meta['SHIB_eppn'] = self.user.username
response = self._get(meta)
self.assertEqual(response.status_code, 302)
self.assertEqual(User.objects.count(), 1)
user = User.objects.first()
self.assertEqual(user.email, 'teemu.teekkari@aalto.fi')
self.assertEqual(user.first_name, 'Teemu')
self.assertEqual(user.last_name, 'Sukunimi')
self.assertEqual(user.userprofile.student_id, '123453')
