def test_ignore_permissions_for_get_filters_cond(self):...
frappe.set_user('test1@example.com')
self.assertRaises(frappe.PermissionError, get_filters_cond, 'DocType', dict
    (istable=1), [])
self.assertTrue(get_filters_cond('DocType', dict(istable=1), [],
    ignore_permissions=True))
frappe.set_user('Administrator')
