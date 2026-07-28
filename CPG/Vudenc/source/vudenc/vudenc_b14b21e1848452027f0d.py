def test_when_logged_in_index_page_redirects_to_dashboard(self):...
self.client.login(username=self.tester.username, password='password')
response = self.client.get(reverse('core-views-index'))
self.assertRedirects(response, reverse('tcms-recent', args=[self.tester.
    username]), target_status_code=HTTPStatus.OK)
