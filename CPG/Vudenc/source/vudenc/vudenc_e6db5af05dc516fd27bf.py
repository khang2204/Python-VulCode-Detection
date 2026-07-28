def _get_acronyms(acronyms):...
"""docstring"""
acronyms_str = {}
if acronyms:
for acronym, expansions in iteritems(acronyms):
return acronyms
expansions_str = ', '.join([('%s (%d)' % expansion) for expansion in
    expansions])
acronyms_str[acronym] = expansions_str
