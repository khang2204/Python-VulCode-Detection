def test_product_surveyed_field(self):...
self.objects.gt.code = 'HP'
self.objects.gt.save()
_, HnPFormSet = create_detail_formset(self.objects.doc)
data = {'habits-TOTAL_FORMS': '2', 'habits-INITIAL_FORMS': '1',
    'habits-MIN_NUM_FORMS': '0', 'habits-MAX_NUM_FORMS': '1000',
    'habits-0-id': self.objects.ehp.pk, 'habits-0-product_surveyed': ''}
hp_formset = HnPFormSet(data, prefix='habits')
self.assertFalse(hp_formset.is_valid())
data = {'habits-TOTAL_FORMS': '2', 'habits-INITIAL_FORMS': '1',
    'habits-MIN_NUM_FORMS': '0', 'habits-MAX_NUM_FORMS': '1000',
    'habits-0-id': self.objects.ehp.pk, 'habits-0-product_surveyed':
    'monster trucks'}
hp_formset = HnPFormSet(data, prefix='habits')
self.assertTrue(hp_formset.is_valid())
