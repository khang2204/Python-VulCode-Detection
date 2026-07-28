def test_course_views(self):...
response = self.client.get('/no_course/test', follow=True)
self.assertEqual(response.status_code, 404)
response = self.client.get(self.current_course_instance.get_absolute_url(),
    follow=True)
self.assertTrue(response.redirect_chain)
self.assertEqual(response.status_code, 200)
self.assertTemplateUsed(response, 'userprofile/login.html')
self.client.login(username='testUser', password='testPassword')
response = self.client.get('/no_course/test', follow=True)
self.assertEqual(response.status_code, 404)
response = self.client.get(self.current_course_instance.get_absolute_url(),
    follow=True)
self.assertEqual(response.status_code, 200)
self.assertEqual(response.context['course'], self.course)
self.assertEqual(response.context['instance'], self.current_course_instance)
self.assertFalse(response.context['is_assistant'])
self.assertFalse(response.context['is_teacher'])
response = self.client.get(self.hidden_course_instance.get_absolute_url(),
    follow=True)
self.assertEqual(response.status_code, 403)
