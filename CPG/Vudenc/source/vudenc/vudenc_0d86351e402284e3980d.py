def test_product(self):...
p = self.objects.p
puc = self.objects.puc
tag = self.objects.pt
PUCToTag.objects.create(content_object=puc, tag=tag)
ProductToPUC.objects.create(product=p, puc=puc)
url = self.live_server_url + f'/product/{p.pk}/'
self.browser.get(url)
submit = self.browser.find_element_by_id('tag_submit')
self.assertFalse(submit.is_enabled(), 'Button should be disabled')
tag = self.browser.find_element_by_class_name('taggit-tag')
tag.click()
self.assertTrue(submit.is_enabled(), 'Button should be enabled')
