def _output_marc(output_complete, categories, kw_field=bconfig....
"""docstring"""
kw_template = """<datafield tag="%s" ind1="%s" ind2="%s">
    <subfield code="2">%s</subfield>
    <subfield code="a">%s</subfield>
    <subfield code="n">%s</subfield>
    <subfield code="9">%s</subfield>
</datafield>
"""
output = []
tag, ind1, ind2 = _parse_marc_code(kw_field)
for keywords in (output_complete['Single keywords'], output_complete[
for kw in keywords:
for field, keywords in ((auth_field, output_complete['Author keywords']), (
output.append(kw_template % (tag, ind1, ind2, encode_for_xml(provenience),
    encode_for_xml(kw), keywords[kw], encode_for_xml(categories[kw])))
if keywords and len(keywords) and field:
return ''.join(output)
tag, ind1, ind2 = _parse_marc_code(field)
for kw, info in keywords.items():
output.append(kw_template % (tag, ind1, ind2, encode_for_xml(provenience),
    encode_for_xml(kw), '', encode_for_xml(categories[kw])))
