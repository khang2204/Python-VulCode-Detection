def test_datagroup(self):...
list_url = self.live_server_url + '/datagroups/'
self.browser.get(list_url)
self.browser.find_element_by_xpath('//*[@title="edit"]').click()
btn = self.browser.find_element_by_name('cancel')
self.assertEqual(btn.get_attribute('href'), list_url,
    'User should go back to list view when clicking cancel')
dg = DataGroup.objects.first()
ds_detail_url = f'{self.live_server_url}/datasource/{dg.data_source.pk}'
self.browser.get(ds_detail_url)
self.browser.find_elements_by_xpath('//*[@title="edit"]')[1].click()
btn = self.browser.find_element_by_name('cancel')
self.assertEqual(btn.get_attribute('href'), ds_detail_url,
    'User should go back to detail view when clicking cancel')
dg_detail_url = f'{self.live_server_url}/datagroup/{dg.pk}/'
self.browser.get(dg_detail_url)
self.browser.find_element_by_xpath('//*[@title="edit"]').click()
btn = self.browser.find_element_by_name('cancel')
self.assertEqual(btn.get_attribute('href'), dg_detail_url,
    'User should go back to detail view when clicking cancel')
edit_url = f'{self.live_server_url}/datagroup/edit/{dg.pk}/'
self.browser.get(edit_url)
self.browser.find_element_by_name('cancel').click()
self.assertIn('/datagroups/', self.browser.current_url,
    'User should always return to detail page after submit')
