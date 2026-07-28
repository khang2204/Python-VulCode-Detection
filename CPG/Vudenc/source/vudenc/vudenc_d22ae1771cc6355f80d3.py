def process_lines():...
if output_mode == 'text':
print('Input file: %s' % source)
output = get_keywords_from_text(text_lines, taxonomy_name, output_mode=
    output_mode, output_limit=output_limit, spires=spires, match_mode=
    match_mode, no_cache=no_cache, with_author_keywords=
    with_author_keywords, rebuild_cache=rebuild_cache, only_core_tags=
    only_core_tags, extract_acronyms=extract_acronyms)
if api:
return output
if isinstance(output, dict):
for i in output:
print(output[i])
