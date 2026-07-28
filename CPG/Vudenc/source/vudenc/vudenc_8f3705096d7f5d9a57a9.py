def parse_html(self, div):...
p_tags = div.find_all('p', not {'class': 'mw-empty-elt'}, recursive=False,
    limit=self.MAX_P_CHECKS)
for p in p_tags:
next_wiki = self.parse_tag(p)
ul = div.find('ul', recursive=False)
if next_wiki:
next_wiki = self.parse_tag(ul)
return next_wiki
return next_wiki
