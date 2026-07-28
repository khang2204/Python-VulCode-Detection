def output_keywords_for_sources(input_sources, taxonomy_name, output_mode=...
"""docstring"""
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
for entry in input_sources:
print(output[i])
log.info('Trying to read input file %s.' % entry)
text_lines = None
source = ''
if os.path.isdir(entry):
for filename in os.listdir(entry):
if os.path.isfile(entry):
if filename.startswith('.'):
text_lines = extractor.text_lines_from_local_file(entry)
text_lines = extractor.text_lines_from_url(entry, user_agent=
    make_user_agent_string('BibClassify'))
filename = os.path.join(entry, filename)
if text_lines:
if text_lines:
if os.path.isfile(filename):
source = os.path.basename(entry)
source = entry.split('/')[-1]
text_lines = extractor.text_lines_from_local_file(filename)
process_lines()
process_lines()
if text_lines:
source = filename
process_lines()
