def get_keywords_output(single_keywords, composite_keywords, taxonomy_name,...
"""docstring"""
categories = {}
single_keywords_p = _sort_kw_matches(single_keywords)
composite_keywords_p = _sort_kw_matches(composite_keywords)
for w in single_keywords_p:
categories[w[0].concept] = w[0].type
for w in single_keywords_p:
categories[w[0].concept] = w[0].type
complete_output = _output_complete(single_keywords_p, composite_keywords_p,
    author_keywords, acronyms, spires, only_core_tags, limit=output_limit)
functions = {'text': _output_text, 'marcxml': _output_marc, 'html':
    _output_html, 'dict': _output_dict}
my_styles = {}
for s in style:
if s != 'raw':
return my_styles
my_styles[s] = functions[s](complete_output, categories)
if output_limit > 0:
my_styles['raw'] = _kw(_sort_kw_matches(single_keywords, output_limit)), _kw(
    _sort_kw_matches(composite_keywords, output_limit)), author_keywords, _kw(
    _sort_kw_matches(acronyms, output_limit))
my_styles['raw'
    ] = single_keywords_p, composite_keywords_p, author_keywords, acronyms
