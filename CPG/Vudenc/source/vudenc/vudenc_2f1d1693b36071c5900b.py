def test_download_raw_comp_data(self):...
dg_co = DataGroup.objects.filter(group_type__code='CO').first()
resp = self.client.get(f'/datagroup/%s/' % dg_co.id)
self.assertIn(b'Download Raw', resp.content)
dg_ids = DataDocument.objects.filter(id__in=ExtractedChemical.objects.all()
    .values('extracted_text_id')).order_by().values_list('data_group_id',
    flat=True).distinct()
for dg_id in dg_ids:
resp = self.client.get(f'/datagroup/raw_extracted_records/%s/' % dg_id)
resp = self.client.get(f'/datagroup/raw_extracted_records/%s/' % dg_ids[0])
self.assertEqual(resp.status_code, 200)
field_list = (
    'ExtractedChemical_id,raw_cas,raw_chem_name,raw_min_comp,raw_central_comp,raw_max_comp,unit_type'
    )
content = list(i.decode('utf-8') for i in resp.streaming_content)
self.assertIn(field_list, content[1])
