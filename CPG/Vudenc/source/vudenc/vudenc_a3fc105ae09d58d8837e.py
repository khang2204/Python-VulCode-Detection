def test_delete_doc_button(self):...
url = f'/datagroup/{DataGroup.objects.first().id}/'
response = self.client.get(url).content.decode('utf8')
span = '<span class="oi oi-trash"></span>'
self.assertIn(span, response, 'Trash button should be present if not matched.')
self.objects.doc.matched = True
self.objects.doc.save()
response = self.client.get(url).content.decode('utf8')
span = '<span class="oi oi-circle-check" style="color:green;"></span>'
self.assertIn(span, response, 'Check should be present if matched.')
