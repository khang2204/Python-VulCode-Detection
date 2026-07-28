def parse_tag(self, tag):...
next_wiki = None
contents = tag.contents
stack = []
for element in contents:
if isinstance(element, NavigableString):
return next_wiki
if '(' in element:
if isinstance(element, Tag) and not stack:
stack.append('(')
if ')' in element:
a_tag = element
stack.pop()
if not getattr(element, 'name', None) == 'a':
a_tag = element.find('a')
if self.is_valid(a_tag):
return a_tag.attrs['href']
