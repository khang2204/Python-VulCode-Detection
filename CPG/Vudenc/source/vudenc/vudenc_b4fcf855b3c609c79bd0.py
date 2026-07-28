def test_dtxsid_dds_n(self):...
dtxs = ['DTXSID9022528', 'DTXSID1020273', 'DTXSID6026296', 'DTXSID2021781']
stats = stats_by_dtxsids(dtxs)
for e in stats:
if e['sid'] == 'DTXSID9022528':
self.assertEqual(2, ethylparaben_stats['dds_n'],
    'There should be 2 datadocuments associated with ethylaraben')
ethylparaben_stats = e
self.client.login(username='Karyn', password='specialP@55word')
dds = DataDocument.objects.filter(pk__in=ExtractedChemical.objects.filter(
    dsstox__sid='DTXSID9022528').values('extracted_text__data_document'))
dd = dds[0]
dd.delete()
stats = stats_by_dtxsids(dtxs)
for e in stats:
if e['sid'] == 'DTXSID9022528':
self.assertEqual(1, ethylparaben_stats['dds_n'],
    'There should now be 1 datadocument associated with ethylaraben')
ethylparaben_stats = e
