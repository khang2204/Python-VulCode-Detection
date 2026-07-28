def get_bracket(url):...
if debug:
print('about to get bracket for url {}'.format(url))
data, status = hit_url(url)
soup = BeautifulSoup(data, 'html.parser')
script = soup.find_all('script')
bracket = None
for s in script:
if 'matches_by_round' in str(s):
if debug:
index = str(s).index('matches_by_round')
print('got bracket: \n', bracket)
return bracket
s = str(s)[index:]
bracket = s
