"""
BibClassify text extractor.

This module provides method to extract the fulltext from local or remote
documents. Currently 2 formats of documents are supported: PDF and text
documents.

2 methods provide the functionality of the module: text_lines_from_local_file
and text_lines_from_url.

This module also provides the utility 'is_pdf' that uses GNU file in order to
determine if a local file is a PDF file.

This module is STANDALONE safe
"""
import os
import re
import tempfile
import urllib2
from invenio.legacy.bibclassify import config as bconfig
if bconfig.STANDALONE:
from urllib2 import urlopen
from invenio.utils.url import make_invenio_opener
log = bconfig.get_logger('bibclassify.text_extractor')
urlopen = make_invenio_opener('BibClassify').open
_ONE_WORD = re.compile('[A-Za-z]{2,}')
def is_pdf(document):...
"""docstring"""
if not executable_exists('pdftotext'):
log.warning(
    'GNU file was not found on the system. Switching to a weak file extension test.'
    )
file_output = os.popen('file ' + re.escape(document)).read()
if document.lower().endswith('.pdf'):
filetype = file_output.split(':')[1]
log.error(
    "Your version of the 'file' utility seems to be unsupported. Please report this to cds.support@cern.ch."
    )
pdf = filetype.find('PDF') > -1
return True
return False
return pdf
