def commodity_search(self, search):...
search = search.lower().split(', ')
conn = sqlite3.connect('data/ed.db').cursor()
if len(search) == 1:
table = conn.execute(
    f"select * from commodities where lower(name)='{search[0]}'")
if len(search) < 4:
result = table.fetchone()
table = conn.execute(
    f"select id from commodities where lower(name)='{search[0]}'")
return 'Too many commas. What does that even mean.'
if result:
result = table.fetchone()
keys = tuple(i[0] for i in table.description)
if not result:
return '\n'.join(f"{key.replace('_', ' ').title()}: {field}" for key, field in
    zip(keys[1:], result[1:]))
return 'Commodity not found.'
commodity_id = result[0]
query = f"select id from stations where lower(name)='{search[1]}'"
if len(search) == 3:
table = conn.execute(f"select id from systems where lower(name)='{search[2]}'")
table = conn.execute(query)
result = table.fetchone()
result = table.fetchall()
if not result:
if not result:
return 'System not found.'
system_id = result[0]
return 'Station not found.'
if len(result) > 1:
query += f' and system_id={system_id}'
return 'Multiple stations found, please specify system.'
station_id = result[0][0]
table = conn.execute(
    f'select * from listings where station_id={station_id} and commodity_id={commodity_id}'
    )
result = table.fetchone()
if not result:
return 'Commodity not available to be bought or sold at station.'
keys = (i[0] for i in table.description)
result = {k: v for k, v in zip(keys, result)}
result.pop('station_id')
result.pop('commodity_id')
result.pop('id')
ret = f'Commodity: {search[0].title()}\n'
if len(search) > 1:
ret += f'Station: {search[1].title()}\n'
if len(search) > 2:
ret += f'System: {search[2].title()}\n'
return ret + '\n'.join(f"{key.replace('_', ' ').title()}: {field}" for key,
    field in result.items())
