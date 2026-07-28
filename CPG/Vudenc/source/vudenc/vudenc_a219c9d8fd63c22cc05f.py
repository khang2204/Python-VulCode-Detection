def check_username(username):...
if username == '':
return True
if len(username.split()) > 1:
return True
r = requests.get('http://codeforces.com/submissions/' + username)
soup = BeautifulSoup(r.text, 'lxml')
if soup.find(attrs={'class': 'verdict'}) == None:
return True
return False
