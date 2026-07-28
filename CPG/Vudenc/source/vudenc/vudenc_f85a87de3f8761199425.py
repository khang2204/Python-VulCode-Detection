@classmethod...
if not keyword:
return []
result = cls.search_keyword('"' + keyword + '"*', lim=limit)[:]
titles = [g.title.lower() for g in result]
all_terms = set()
for line in titles:
if len(all_terms) >= max_terms:
return list(all_terms)
i1 = line.find(keyword)
i2 = line.find(' ', i1 + len(keyword))
term = line[i1:i2] if i2 >= 0 else line[i1:]
if term != keyword:
all_terms.add(term)
