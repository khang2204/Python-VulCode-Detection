def is_valid(html, url=None):...
errors = ["The page you're looking for isn't here", 'No tournaments found',
    'Internal Server Error', 'Not Implemented', 'Bad Gateway',
    'Gateway Time-out', 'Gateway Timeout', 'Service Unavailable',
    'Gateway Timeout', 'HTTP Version Not Supported',
    'Variant Also Negotiates', 'Insufficient Storage', 'Loop Detected',
    'Not Extended', 'Network Authentication Required']
for error in errors:
if error.lower() in str(html).lower():
if 'member since' in str(html).lower():
if debug:
return True
if 'organizations' in str(html).lower():
print('page invalid, found error string {}'.format(error))
return False
return True
if url and 'standings' in url:
return True
return bracket_complete(html)
