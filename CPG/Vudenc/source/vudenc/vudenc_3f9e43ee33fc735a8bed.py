def build_marc(recid, single_keywords, composite_keywords, spires=False,...
"""docstring"""
output = [
    """<collection><record>
<controlfield tag="001">%s</controlfield>""" %
    recid]
single_keywords = single_keywords.items()
composite_keywords = composite_keywords.items()
output.append(_output_marc(single_keywords, composite_keywords,
    author_keywords, acronyms))
output.append('</record></collection>')
return '\n'.join(output)
