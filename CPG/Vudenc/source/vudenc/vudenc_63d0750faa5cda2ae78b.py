def run_custom_query(self, query):...
if '%(key)s' in query:
query = query.replace('%(key)s', 'name')
return frappe.db.sql(query, as_dict=not self.as_list)
