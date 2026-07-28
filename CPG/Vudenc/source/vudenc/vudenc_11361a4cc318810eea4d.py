def _get_prefixed_value(self, lines, prefix):...
for line in lines:
if line.startswith(prefix):
return
return line[len(prefix):]
