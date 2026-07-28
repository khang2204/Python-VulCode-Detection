def test_dtxsid_pucs_n(self):...
dtxs = ['DTXSID9022528', 'DTXSID1020273', 'DTXSID6026296', 'DTXSID2021781']
stats = stats_by_dtxsids(dtxs)
ethylparaben_stats = stats.get(sid='DTXSID9022528')
self.assertEqual(0, ethylparaben_stats['pucs_n'])
self.client.login(username='Karyn', password='specialP@55word')
dds = DataDocument.objects.filter(pk__in=ExtractedChemical.objects.filter(
    dsstox__sid='DTXSID9022528').values('extracted_text__data_document'))
dd = dds[0]
ds = dd.data_group.data_source
p = Product.objects.create(data_source=ds, title='Test Product', upc=
    'Test UPC for ProductToPUC')
pd = ProductDocument.objects.create(document=dd, product=p)
pd.save()
dd.refresh_from_db()
pid = dd.products.first().pk
puc = PUC.objects.get(id=20)
ppuc = ProductToPUC.objects.create(product=Product.objects.get(pk=pid), puc
    =puc, puc_assigned_usr=User.objects.get(username='Karyn'))
ppuc.refresh_from_db()
stats = stats_by_dtxsids(dtxs)
ethylparaben_stats = stats.get(sid='DTXSID9022528')
self.assertEqual(1, ethylparaben_stats['pucs_n'])
