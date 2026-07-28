def test_query_fields_sanitizer(self):...
self.assertRaises(frappe.DataError, DatabaseQuery('DocType').execute,
    fields=['name', 'issingle, version()'], limit_start=0, limit_page_length=1)
self.assertRaises(frappe.DataError, DatabaseQuery('DocType').execute,
    fields=['name',
    'issingle, IF(issingle=1, (select name from tabUser), count(name))'],
    limit_start=0, limit_page_length=1)
self.assertRaises(frappe.DataError, DatabaseQuery('DocType').execute,
    fields=['name', 'issingle, (select count(*) from tabSessions)'],
    limit_start=0, limit_page_length=1)
self.assertRaises(frappe.DataError, DatabaseQuery('DocType').execute,
    fields=['name',
    "issingle, SELECT LOCATE('', `tabUser`.`user`) AS user;"], limit_start=
    0, limit_page_length=1)
self.assertRaises(frappe.DataError, DatabaseQuery('DocType').execute,
    fields=['name',
    'issingle, IF(issingle=1, (SELECT name from tabUser), count(*))'],
    limit_start=0, limit_page_length=1)
data = DatabaseQuery('DocType').execute(fields=['name', 'issingle',
    'count(name)'], limit_start=0, limit_page_length=1)
self.assertTrue('count(name)' in data[0])
data = DatabaseQuery('DocType').execute(fields=['name', 'issingle',
    "locate('', name) as _relevance"], limit_start=0, limit_page_length=1)
self.assertTrue('_relevance' in data[0])
data = DatabaseQuery('DocType').execute(fields=['name', 'issingle',
    'date(creation) as creation'], limit_start=0, limit_page_length=1)
self.assertTrue('creation' in data[0])
data = DatabaseQuery('DocType').execute(fields=['name', 'issingle',
    'datediff(modified, creation) as date_diff'], limit_start=0,
    limit_page_length=1)
self.assertTrue('date_diff' in data[0])
