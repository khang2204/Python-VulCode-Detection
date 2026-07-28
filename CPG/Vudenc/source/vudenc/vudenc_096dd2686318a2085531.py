def test_in_not_in_filters(self):...
self.assertFalse(DatabaseQuery('DocType').execute(filters={'name': ['in',
    None]}))
self.assertTrue({'name': 'DocType'} in DatabaseQuery('DocType').execute(
    filters={'name': ['not in', None]}))
for result in [{'name': 'DocType'}, {'name': 'DocField'}]:
self.assertTrue(result in DatabaseQuery('DocType').execute(filters={'name':
    ['in', 'DocType,DocField']}))
for result in [{'name': 'DocType'}, {'name': 'DocField'}]:
self.assertFalse(result in DatabaseQuery('DocType').execute(filters={'name':
    ['not in', 'DocType,DocField']}))
