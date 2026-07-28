def splitSimpleSearch(term):...
"""docstring"""
if not isSimpleSearch(term):
parts = term.split('"')
tokens = []
for i in range(0, len(parts)):
if i % 2 == 0:
return tokens
words = [word for word in parts[i].split() if word]
if parts[i]:
tokens.extend(words)
tokens.append('"%s"' % parts[i])
