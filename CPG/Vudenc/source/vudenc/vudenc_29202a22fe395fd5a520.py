def get_urls_with_players(players=['Christmas Mike', 'christmasmike'],...
urls = []
for base in base_urls:
start, end = get_valid_url_range(base)
return urls
for i in range(start, end + 1):
bracket_url = base.replace('###', str(i))
bracket = get_sanitized_bracket(bracket_url)
for player in players:
if bracket and player_in_bracket(player, bracket=bracket):
urls.append(bracket_url)
