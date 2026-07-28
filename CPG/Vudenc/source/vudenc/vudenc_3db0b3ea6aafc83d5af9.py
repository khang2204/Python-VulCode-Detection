def test_dtxsid_dds_wf_n(self):...
dtxs = ['DTXSID9022528', 'DTXSID1020273', 'DTXSID6026296', 'DTXSID2021781']
stats = stats_by_dtxsids(dtxs)
for e in stats:
if e['sid'] == 'DTXSID9022528':
self.assertEqual(1, ethylparaben_stats['dds_wf_n'],
    'There should be 1 extracted chemical         with weight fraction data associated with ethylparaben'
    )
ethylparaben_stats = e
ec = ExtractedChemical.objects.get(rawchem_ptr_id=73)
ec.raw_min_comp = 0.1
ec.save()
stats = stats_by_dtxsids(dtxs)
for e in stats:
if e['sid'] == 'DTXSID9022528':
self.assertEqual(2, ethylparaben_stats['dds_wf_n'],
    'There should be 2 extracted chemicals         with weight fraction data associated with ethylparaben'
    )
ethylparaben_stats = e
