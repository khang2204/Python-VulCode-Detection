def text_lines_from_local_file(document, remote=False):...
"""docstring"""
if is_pdf(document):
log.error('Unable to read from file %s. (%s)' % (document, ex1.strerror))
lines = [line.decode('utf-8', 'replace') for line in filestream]
if not executable_exists('pdftotext'):
filestream = open(document, 'r')
return []
filestream.close()
log.error('pdftotext is not available on the system.')
cmd = 'pdftotext -q -enc UTF-8 %s -' % re.escape(document)
if not _is_english_text('\n'.join(lines)):
filestream = os.popen(cmd)
log.warning(
    "It seems the file '%s' is unvalid and doesn't contain text. Please communicate this file to the Invenio team."
     % document)
line_nb = len(lines)
word_nb = 0
for line in lines:
word_nb += len(re.findall('\\S+', line))
lines = [line for line in lines if _ONE_WORD.search(line) is not None]
if not remote:
log.info('Local file has %d lines and %d words.' % (line_nb, word_nb))
return lines
