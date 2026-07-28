def get_display_base(url, counter=None):...
if 'challonge' in url:
html, _ = hit_url(url)
d_map = constants.DISPLAY_MAP
soup = BeautifulSoup(html, 'html.parser')
for k in d_map:
display_name = soup.find('div', {'id': 'title'})
if k.lower() in url.lower():
if 'smash.gg' in url:
if display_name and hasattr(display_name, 'title'):
base = d_map[k]
parts = url.split('event')[0].split('/')[-2].split('-')
return url
title = display_name.text.rstrip().lstrip()
LOG.info('url {} has no title'.format(url))
if counter:
display_list = [s.title() for s in parts]
name = re.sub('[^a-z A-Z 0-9 # / \\ .]', '', title)
display_name = soup.find('h1', {'class': 'title'})
name = '{} {}'.format(base, counter)
return base
return ' '.join(display_list)
return name
if display_name:
return name
name = display_name.find(text=True).lstrip().rstrip()
LOG.info('just found new title for url: {} - {}'.format(url, name))
return name
