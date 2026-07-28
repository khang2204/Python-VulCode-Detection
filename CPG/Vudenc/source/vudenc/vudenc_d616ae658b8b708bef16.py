def _get_fieldcodes(skw_matches, ckw_matches, spires=False):...
"""docstring"""
fieldcodes = {}
output = {}
for skw, _ in skw_matches:
for fieldcode in skw.fieldcodes:
for ckw, _ in ckw_matches:
fieldcodes.setdefault(fieldcode, set()).add(skw.output(spires))
if len(ckw.fieldcodes):
for fieldcode, keywords in fieldcodes.items():
for fieldcode in ckw.fieldcodes:
for kw in ckw.getComponents():
output[fieldcode] = ', '.join(keywords)
return output
fieldcodes.setdefault(fieldcode, set()).add(ckw.output(spires))
for fieldcode in kw.fieldcodes:
fieldcodes.setdefault(fieldcode, set()).add('%s*' % ckw.output(spires))
fieldcodes.setdefault('*', set()).add(kw.output(spires))
