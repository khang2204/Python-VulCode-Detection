def get_failed_paths(self, search=None):...
"""docstring"""
search = convert_search(search)
fetch_ok = self.execute(
    "SELECT path FROM history WHERE name LIKE ? AND status = 'Failed'", (
    search,))
if fetch_ok:
return [item.get('path') for item in self.c.fetchall()]
return []
