def test_qa_begin(self):...
"""docstring"""
self.assertFalse(Script.objects.get(pk=5).qa_begun,
    'The Script should have qa_begun of False at the beginning')
response = self.client.get('/qa/extractionscript/5/')
self.assertTrue(Script.objects.get(pk=5).qa_begun,
    'qa_begun should now be true')
