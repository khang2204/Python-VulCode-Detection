def setUp(self):...
self.user = User(username='meikalm8@aalto.fi', email='', first_name='Matti',
    last_name='Sukunimi')
self.user.set_unusable_password()
self.user.save()
self.user.userprofile.student_id = '000'
self.user.userprofile.save()
self.login_url = reverse('shibboleth-login')
