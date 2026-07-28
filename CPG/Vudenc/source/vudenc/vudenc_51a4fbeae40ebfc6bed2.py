def _get_partial_text(fulltext):...
"""docstring"""
length = len(fulltext)
get_index = lambda x: int(float(x) / 100 * length)
partial_text = [fulltext[get_index(start):get_index(end)] for start, end in
    bconfig.CFG_BIBCLASSIFY_PARTIAL_TEXT]
return '\n'.join(partial_text)
