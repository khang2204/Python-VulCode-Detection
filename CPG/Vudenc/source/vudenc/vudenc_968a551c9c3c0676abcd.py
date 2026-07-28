def get_bracket_urls_from_scene(scene_url, load_from_cache=True):...
scene_brackets_html, status = hit_url(scene_url, load_from_cache=
    load_from_cache)
scene_name = scene_url.split('https://')[-1].split('.')[0]
soup = BeautifulSoup(scene_brackets_html, 'html.parser')
links = soup.find_all('a')
bracket_links = []
for link in links:
if link.has_attr('href') and scene_name in link['href']:
return bracket_links
html = get_bracket(link['href'])
if html and is_valid(html, url=link['href']):
bracket_links.append(link['href'])
if total and len(bracket_links) >= total:
return bracket_links
