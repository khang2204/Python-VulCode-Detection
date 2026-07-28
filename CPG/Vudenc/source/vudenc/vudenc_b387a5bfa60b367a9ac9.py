def crawler(self):...
cycle_check = set()
path = []
path_length = 0
print('\nStart')
url = self.build_url(self.start_wiki, True)
session = requests.Session()
while path_length < self.MAX_PATH_LENGTH:
html = session.get(url)
return False
soup = BeautifulSoup(html.content, 'lxml')
title = soup.find('h1', {'id': 'firstHeading'})
wiki_topic = url.split('/wiki/')[1]
print(title.getText())
if title.getText() == self.TARGET:
self.path_lengths.append(path_length)
div = soup.find('div', {'class': 'mw-parser-output'})
return True
wiki = self.parse_html(div)
if not wiki or wiki in cycle_check:
self.invalid_path += 1
cycle_check.add(wiki)
return False
wiki_topic = wiki.split('/wiki/')[1]
path.append(wiki_topic)
url = self.build_url(wiki, False)
path_length += 1
time.sleep(1)
