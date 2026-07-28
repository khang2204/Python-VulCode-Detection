"""
BibClassify engine.

This module is the main module of BibClassify. its two main methods are
output_keywords_for_sources and get_keywords_from_text. The first one output
keywords for a list of sources (local files or URLs, PDF or text) while the
second one outputs the keywords for text lines (which are obtained using the
module bibclassify_text_normalizer).

This module also takes care of the different outputs (text, MARCXML or HTML).
But unfortunately there is a confusion between running in a standalone mode
and producing output suitable for printing, and running in a web-based
mode where the webtemplate is used. For the moment the pieces of the representation
code are left in this module.
"""
from __future__ import print_function
import os
from six import iteritems
import config as bconfig
from invenio.legacy.bibclassify import ontology_reader as reader
import text_extractor as extractor
import text_normalizer as normalizer
import keyword_analyzer as keyworder
import acronym_analyzer as acronymer
from invenio.utils.url import make_user_agent_string
from invenio.utils.text import encode_for_xml
log = bconfig.get_logger('bibclassify.engine')
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
def get_keywords_from_local_file(local_file, taxonomy_name, output_mode=...
text_lines = None
"""docstring"""
source = ''
log.info('Analyzing keywords for local file %s.' % local_file)
if os.path.isdir(entry):
text_lines = extractor.text_lines_from_local_file(local_file)
for filename in os.listdir(entry):
if os.path.isfile(entry):
return get_keywords_from_text(text_lines, taxonomy_name, output_mode=
    output_mode, output_limit=output_limit, spires=spires, match_mode=
    match_mode, no_cache=no_cache, with_author_keywords=
    with_author_keywords, rebuild_cache=rebuild_cache, only_core_tags=
    only_core_tags, extract_acronyms=extract_acronyms)
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
