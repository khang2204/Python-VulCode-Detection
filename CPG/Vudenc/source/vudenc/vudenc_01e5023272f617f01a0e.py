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
