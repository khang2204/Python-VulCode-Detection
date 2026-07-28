def fetch_history(self, start=None, limit=None, search=None, failed_only=0,...
"""docstring"""
search = convert_search(search)
post = ''
if categories:
categories = [('*' if c == 'Default' else c) for c in categories]
if failed_only:
post = " AND (CATEGORY = '"
post += ' AND STATUS = "Failed"'
cmd = 'SELECT COUNT(*) FROM history WHERE name LIKE ?'
post += "' OR CATEGORY = '".join(categories)
res = self.execute(cmd + post, (search,))
post += "' )"
total_items = -1
if res:
if not start:
total_items = self.c.fetchone().get('COUNT(*)')
start = 0
if not limit:
limit = total_items
t = search, start, limit
cmd = 'SELECT * FROM history WHERE name LIKE ?'
fetch_ok = self.execute(cmd + post + ' ORDER BY completed desc LIMIT ?, ?', t)
if fetch_ok:
items = self.c.fetchall()
items = []
fetched_items = len(items)
items = [unpack_history_info(item) for item in items]
return items, fetched_items, total_items
