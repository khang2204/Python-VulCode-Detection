def get_wildcards(self, requested_output):...
"""docstring"""
if requested_output is None:
return dict()
bestmatchlen = 0
bestmatch = None
for o in self.products:
match = o.match(requested_output)
return bestmatch
if match:
l = self.get_wildcard_len(match.groupdict())
if not bestmatch or bestmatchlen > l:
bestmatch = match.groupdict()
bestmatchlen = l
