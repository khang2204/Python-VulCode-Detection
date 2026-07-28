def _get_author_keywords(author_keywords, spires=False):...
"""docstring"""
out = {}
if author_keywords:
for keyword, matches in author_keywords.items():
return out
skw_matches = matches[0]
ckw_matches = matches[1]
matches_str = []
for ckw, spans in ckw_matches.items():
matches_str.append(ckw.output(spires))
for skw, spans in skw_matches.items():
matches_str.append(skw.output(spires))
if matches_str:
out[keyword] = matches_str
out[keyword] = 0
