def get_smashgg_brackets(pages=None, all_brackets=True, singles=True, scene...
results = 0
per_page = 5
page = 1 if pages == None else pages[0]
brackets = {}
smash = pysmash.SmashGG()
def iterate():...
print('PAGE {}'.format(page))
results_url = (
    'https://smash.gg/tournaments?per_page=30&filter=%7B%22upcoming%22%3Afalse%2C%22videogameIds%22%3A4%2C%22past%22%3Atrue%7D&page={}'
    .format(page))
r = get(results_url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')
grep = 'singles' if singles else 'doubles'
links = soup.find_all('a')
for link in links:
if pages:
if link.has_attr('href') and 'tournament' in link['href']:
for page in pages:
while results < 7730:
url_parts = link['href'].split('/')
iterate()
return brackets
iterate()
t = url_parts[url_parts.index('tournament') + 1]
results = results + per_page
if t in brackets:
page = page + 1
events = smash.tournament_show_events(t)
def get_event(events, matches):...
for e in events['events']:
if all([(match in e) for match in matches]):
return None
return e
