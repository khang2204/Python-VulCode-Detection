def test_extractedsubclasses(self):...
"""docstring"""
for doc in DataDocument.objects.all():
extsub = ExtractedText.objects.get_subclass(data_document=doc)
if doc.data_group.group_type.code == 'CP':
self.assertEqual(type(extsub), ExtractedCPCat)
if doc.data_group.group_type.code == 'HH':
self.assertEqual(type(extsub), ExtractedHHDoc)
self.assertEqual(type(extsub), ExtractedText)
