def test_download_raw_chem_button(self):...
response = self.client.get('/get_data/')
self.assertEqual(response.status_code, 200)
self.assertContains(response, 'Download Uncurated Chemicals')
rc = RawChem.objects.filter(dsstox_id__isnull=True).first()
response = self.client.get('/dl_raw_chems/')
rc_row = f'%s,%s,%s,%s\r\n' % (rc.id, rc.raw_cas, rc.raw_chem_name, rc.rid if
    rc.rid else '')
rc_row = bytes(rc_row, 'utf-8')
self.assertIn(rc_row, response.content, 'The non-curated row should appear')
rc_row = f'%s,%s,%s,%s,%s\r\n' % (rc.extracted_text.data_document.
    data_group.id, rc.id, rc.raw_cas, rc.raw_chem_name, rc.rid if rc.rid else
    '')
rc_row = bytes(rc_row, 'utf-8')
self.assertIn(rc_row, response.content,
    'The data group id should be in the output')
rc = RawChem.objects.filter(dsstox_id__isnull=False).first()
rc_row = f'%s,%s,%s,%s\r\n' % (rc.id, rc.raw_cas, rc.raw_chem_name, rc.sid if
    rc.sid else '')
rc_row = bytes(rc_row, 'utf-8')
self.assertNotIn(rc_row, response.content, 'The curated row should not appear')
