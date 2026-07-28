def test_detail_template_fieldnames(self):...
pk = self.objects.dg.pk
self.assertEqual(str(self.objects.dg.group_type), 'Composition',
    'Type of DataGroup needs to be "composition" for this test.')
response = self.client.get(f'/datagroup/{pk}/')
self.assertEqual(response.context['extract_fields'], ['data_document_id',
    'data_document_filename', 'prod_name', 'doc_date', 'rev_num',
    'raw_category', 'raw_cas', 'raw_chem_name', 'report_funcuse',
    'raw_min_comp', 'raw_max_comp', 'unit_type', 'ingredient_rank',
    'raw_central_comp'], 'Fieldnames passed are incorrect!')
self.objects.gt.title = 'Functional use'
self.objects.gt.code = 'FU'
self.objects.gt.save()
self.assertEqual(str(self.objects.dg.group_type), 'Functional use',
    'Type of DataGroup needs to be "FU" for this test.')
response = self.client.get(f'/datagroup/{pk}/')
self.assertEqual(response.context['extract_fields'], ['data_document_id',
    'data_document_filename', 'prod_name', 'doc_date', 'rev_num',
    'raw_category', 'raw_cas', 'raw_chem_name', 'report_funcuse'],
    'Fieldnames passed are incorrect!')
