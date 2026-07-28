def test_download_pucs_button(self):...
response = self.client.get('/get_data/')
self.assertEqual(response.status_code, 200)
self.assertContains(response, 'Download PUCs')
