def _find_breakpoints(self, line):...
breakpoints = []
in_quote = False
for i, ch in enumerate(line):
if ch in ['"', "'"]:
return breakpoints
in_quote = not in_quote
if ch == ';' and not in_quote:
breakpoints.append(i)
if ch == '#' and not in_quote:
