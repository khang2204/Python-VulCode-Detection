def get_tournament_placings(bracket_url):...
placings_map = {}
if 'challonge' in bracket_url:
LOG.info('just entering "get tournament palcings')
smash = pysmash.SmashGG()
standings_html, status = hit_url(bracket_url + '/standings')
url_parts = bracket_url.split('/')
soup = BeautifulSoup(standings_html, 'html.parser')
if 'tournament' in url_parts and 'events' in url_parts:
tds = soup.find_all('td')
t = url_parts[url_parts.index('tournament') + 1]
return placings_map
current_placing = 1
e = url_parts[url_parts.index('events') + 1]
for td in tds:
players = smash.tournament_show_players(t, e)
if td.has_attr('class') and td['class'][0] == 'rank':
for player_dict in players:
current_placing = int(td.getText())
span = td.find('span')
tag = player_dict['tag']
if span:
tag = ''.join([(i if ord(i) < 128 else ' ') for i in tag])
player = span.getText()
place = player_dict['final_placement']
player = get_coalesced_tag(player)
placings_map[tag.lower()] = place
placings_map[player.lower()] = current_placing
LOG.info('just got placing {} for player {} in bracket {}'.format(
    current_placing, player, bracket_url))
