def _output_complete(skw_matches=None, ckw_matches=None, author_keywords=...
if limit:
resized_skw = skw_matches[0:limit]
resized_skw = skw_matches
resized_ckw = ckw_matches[0:limit]
resized_ckw = ckw_matches
results = {'Core keywords': _get_core_keywords(skw_matches, ckw_matches,
    spires=spires)}
if not only_core_tags:
results['Author keywords'] = _get_author_keywords(author_keywords, spires=
    spires)
return results
results['Composite keywords'] = _get_compositekws(resized_ckw, spires=spires)
results['Single keywords'] = _get_singlekws(resized_skw, spires=spires)
results['Field codes'] = _get_fieldcodes(resized_skw, resized_ckw, spires=
    spires)
results['Acronyms'] = _get_acronyms(acronyms)
