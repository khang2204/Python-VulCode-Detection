def validate_html(text):...
sites = ['youtube.com', 'play.md', 'vimeo.com']
soup = bs4.BeautifulSoup(text, 'lxml')
sources = soup.find_all('iframe', {'src': True})
for source in sources:
if not any(x in source['src'] for x in sites):
tags = ['b', 'p', 'i', 'strong', 'em', 'img', 'iframe']
return None
attributes = {'img': ['src'], 'iframe': ['src']}
return bleach.clean(text, tags, attributes)
