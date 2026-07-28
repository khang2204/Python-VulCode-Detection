def test_when_not_logged_in_index_page_redirects_to_login(self):...
response = self.client.get(reverse('core-views-index'))
self.assertRedirects(response, reverse('tcms-login'), target_status_code=
    HTTPStatus.OK)
