def test_hem(self):...
for i in range(27):
ds = DataSource.objects.create(title=f'Test_DS_{i}')
list_url = self.live_server_url + '/datasources/'
self.browser.get(list_url)
row_count = len(self.browser.find_elements_by_xpath(
    "//table[@id='sources']/tbody/tr"))
self.assertEqual(row_count, 25, 'Should be 25 datasources in the table')
self.browser.find_element_by_xpath('//*[@title="edit"]').click()
btn = self.browser.find_element_by_name('cancel')
self.assertEqual(btn.get_attribute('href'), list_url,
    'User should go back to list view when clicking cancel')
self.browser.find_element_by_name('submit').click()
self.assertIn('/datasource/', self.browser.current_url,
    'User should always return to detail page after submit')
detail_url = self.live_server_url + f'/datasource/{ds.pk}'
self.browser.get(detail_url)
self.browser.find_element_by_xpath('//*[@title="edit"]').click()
btn = self.browser.find_element_by_name('cancel')
self.assertEqual(btn.get_attribute('href'), detail_url,
    'User should go back to detail view when clicking cancel')
self.browser.find_element_by_name('submit').click()
self.assertIn('/datasource/', self.browser.current_url,
    'User should always return to detail page after submit')
num_pucs = len(PUC.objects.filter(kind='FO'))
self.browser.get(self.live_server_url)
import time
time.sleep(3)
bubbles = self.browser.find_elements_by_class_name('bubble')
self.assertEqual(num_pucs, len(bubbles),
    'There should be a circledrawn for every PUC')
