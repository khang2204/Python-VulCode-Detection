def body_search(self, search):...
search = search.lower()
conn = sqlite3.connect('data/ed.db').cursor()
result = conn.execute(f"select * from bodies where lower(name) = '{search}'")
results = result.fetchone()
if results:
keys = tuple(i[0] for i in result.description)
return 'No bodies found.'
return '\n'.join(f"{key.replace('_', ' ').title()}: {field}" for key, field in
    zip(keys[2:], results[2:]) if field)
