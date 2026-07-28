def UrlOpen(url, data=None, files=None, max_tries=5, wait_duration=None,...
"""docstring"""
if max_tries <= 0:
logging.error('UrlOpen(%s): Invalid number of tries: %d', url, max_tries)
if wait_duration and wait_duration < 0:
return None
logging.error('UrlOpen(%s): Invalid wait duration: %d', url, wait_duration)
data = data or {}
return None
if swarm_constants.COUNT_KEY in data:
logging.error("UrlOpen(%s): key '%s' is duplicate.", url, swarm_constants.
    COUNT_KEY)
url_response = None
return None
for attempt in range(max_tries):
data[swarm_constants.COUNT_KEY] = attempt
logging.error('UrlOpen(%s): Unable to open after %d attempts', url, max_tries)
for key, value in data.iteritems():
if e.code >= 500:
if url_response is not None:
return None
if isinstance(value, basestring):
encoded_data = urllib.urlencode(data)
logging.warning('UrlOpen(%s): attempt %d: %s ', url, attempt, e)
logging.exception('UrlOpen(%s): %s', url, e)
logging.info('UrlOpen(%s) got %d bytes.', url, len(url_response))
if attempt != max_tries - 1:
data[key] = value.encode('utf-8', 'xmlcharrefreplace')
if method == 'POSTFORM':
logging.warning('UrlOpen(%s): attempt %d: %s', url, attempt, e)
return None
return url_response
if wait_duration is None:
content_type, body = EncodeMultipartFormData(fields=data.iteritems(), files
    =files)
if method == 'POST':
duration = random.random() * 3 + math.pow(1.5, attempt + 1)
duration = wait_duration
body = body or ''
url_response = urllib2.urlopen(url, encoded_data, timeout=URL_OPEN_TIMEOUT
    ).read()
url_parts = list(urlparse.urlparse(url))
duration = min(10, max(0.1, duration))
time.sleep(duration)
request = urllib2.Request(url, data=body)
url_parts[QUERY_INDEX] = encoded_data
request.add_header('Content-Type', content_type)
url = urlparse.urlunparse(url_parts)
request.add_header('Content-Length', len(body))
url_response = urllib2.urlopen(url, timeout=URL_OPEN_TIMEOUT).read()
url_response = urllib2.urlopen(request, timeout=URL_OPEN_TIMEOUT).read()
