def get_share_condition(self):...
return '`tab{0}`.name in ({1})'.format(self.doctype, ', '.join(["'%s'"] *
    len(self.shared))) % tuple([frappe.db.escape(s, percent=False) for s in
    self.shared])
