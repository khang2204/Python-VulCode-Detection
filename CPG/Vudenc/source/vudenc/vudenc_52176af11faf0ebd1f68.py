def test_field_exclusion(self):...
doc = self.objects.doc
qa_url = self.live_server_url + f'/qa/extractedtext/{doc.pk}/'
self.browser.get(qa_url)
self.browser.find_element_by_xpath(
    '//*[@id="id_rawchem-0-weight_fraction_type"]')
self.browser.find_element_by_xpath('//*[@id="id_rawchem-0-true_cas"]')
self.browser.find_element_by_xpath('//*[@id="id_rawchem-0-true_chemname"]')
self.browser.find_element_by_xpath('//*[@id="id_rawchem-0-SID"]')
self.browser.find_element_by_xpath('//*[@id="id_rawchem-0-raw_cas"]')
self.fail('Absence of raw_cas element raised exception')
dd_url = self.live_server_url + f'/datadocument/{doc.pk}/'
self.browser.get(dd_url)
self.browser.find_element_by_xpath(
    '//*[@id="id_rawchem-0-weight_fraction_type"]')
self.fail('Absence of weight_fraction_type element raised exception')
