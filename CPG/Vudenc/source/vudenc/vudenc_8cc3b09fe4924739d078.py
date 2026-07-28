def get_cve_cwe_map(self, ids):...
"""docstring"""
if not ids:
return []
query = (
    'SELECT cve_id, cwe.name, cwe.link FROM cve_cwe map JOIN cwe ON map.cwe_id = cwe.id WHERE map.cve_id IN %s'
    )
self.cursor.execute(query, [tuple(ids)])
return self.cursor.fetchall()
