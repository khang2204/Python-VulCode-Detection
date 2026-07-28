def system_search(self, search):...
search = search.lower()
conn = sqlite3.connect('data/ed.db').cursor()
table = conn.execute(f"select * from populated where lower(name) = '{search}'")
results = table.fetchone()
if not results:
table = conn.execute(f"select * from systems where lower(name) = '{search}'")
if results:
results = table.fetchone()
keys = tuple(i[0] for i in table.description)
return 'No systems found.'
return '\n'.join(f"{key.replace('_', ' ').title()}: {field}" for key, field in
    zip(keys[1:], results[1:]) if field)
