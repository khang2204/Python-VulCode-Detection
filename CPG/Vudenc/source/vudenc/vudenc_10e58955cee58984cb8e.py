def test_add_extracted(self):...
"""docstring"""
doc = DataDocument.objects.get(pk=354784)
self.assertFalse(doc.extracted, 'This document is matched but not extracted')
data = {'hhe_report_number': ['47']}
response = self.client.post('/extractedtext/edit/354784/', data=data,
    follow=True)
doc = DataDocument.objects.get(pk=354784)
self.assertTrue(doc.extracted, 'This document is not extracted ')
page = html.fromstring(response.content)
hhe_no = page.xpath('//dd[contains(@class, "hh-report-no")]')[0].text
self.assertIn('47', hhe_no)
