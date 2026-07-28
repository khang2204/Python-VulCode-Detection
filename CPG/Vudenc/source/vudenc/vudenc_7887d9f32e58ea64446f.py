def test_edit_hnp_detail(self):...
self.objects.exscript.title = 'Manual (dummy)'
self.objects.exscript.save()
self.client.login(username='Karyn', password='specialP@55word')
pk = self.objects.doc.pk
response = self.client.get(f'/habitsandpractices/{pk}/')
self.assertNotContains(response, 'Raw Category', html=True)
self.assertContains(response,
    f'href="/datagroup/{self.objects.dg.pk}/" role="button">Cancel</a>')
self.assertContains(response,
    f'href="/datagroup/{self.objects.dg.pk}/" role="button">Back</a>')
response2 = self.client.get(f'/datagroup/{self.objects.dg.pk}/')
self.assertContains(response2, 'Data Group Detail: Data Group for Test')
