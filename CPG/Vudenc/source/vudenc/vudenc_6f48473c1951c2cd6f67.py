def get_token(html, token_name):...
"""docstring"""
soup = bs4.BeautifulSoup(html, 'html.parser')
res = soup.select('[name={}]'.format(token_name))
if not res:
print("Token '{}' not found in html text.".format(token_name))
return res[0]['value']
return ''
