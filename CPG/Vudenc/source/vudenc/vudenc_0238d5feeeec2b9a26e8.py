def text_lines_from_url(url, user_agent=''):...
"""docstring"""
request = urllib2.Request(url)
if user_agent:
request.add_header('User-Agent', user_agent)
distant_stream = urlopen(request)
log.error('Unable to read from URL %s.' % url)
lines = text_lines_from_local_file(local_file, remote=True)
local_file = tempfile.mkstemp(prefix='bibclassify.')[1]
return None
os.remove(local_file)
local_stream = open(local_file, 'w')
line_nb = len(lines)
local_stream.write(distant_stream.read())
word_nb = 0
local_stream.close()
for line in lines:
word_nb += len(re.findall('\\S+', line))
log.info('Remote file has %d lines and %d words.' % (line_nb, word_nb))
return lines
