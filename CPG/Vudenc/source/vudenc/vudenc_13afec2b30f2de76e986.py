def test_or_filters(self):...
data = DatabaseQuery('DocField').execute(filters={'parent': 'DocType'},
    fields=['fieldname', 'fieldtype'], or_filters=[{'fieldtype': 'Table'},
    {'fieldtype': 'Select'}])
self.assertTrue({'fieldtype': 'Table', 'fieldname': 'fields'} in data)
self.assertTrue({'fieldtype': 'Select', 'fieldname': 'document_type'} in data)
self.assertFalse({'fieldtype': 'Check', 'fieldname': 'issingle'} in data)
