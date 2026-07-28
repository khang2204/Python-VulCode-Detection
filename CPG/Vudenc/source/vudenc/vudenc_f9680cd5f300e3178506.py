def station_search(self, search, target_system=None, ctx=None):...
search = search.lower()
conn = sqlite3.connect('data/ed.db').cursor()
if ',' in search:
search, target_system = (i.strip() for i in search.split(','))
query = f"select * from stations where lower(name) = '{search}'"
if target_system is not None:
target_system = target_system.lower()
result = conn.execute(query)
table = conn.execute(
    f"select id from populated where lower(name)='{target_system}'")
results = result.fetchall()
results = table.fetchone()
if len(results) == 1:
if results:
keys = tuple(i[0] for i in result.description)
if not results:
target_system = results[0]
return 'System not found.'
return '\n'.join(f"{key.replace('_', ' ').title()}: {field}" for key, field in
    zip(keys[2:], results[0][2:]) if field)
return 'Station not found.'
return 'Multiple stations found, please specify system.'
query += f' and system_id = {target_system}'
