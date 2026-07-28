def specific_info(self):...
res = 'URL: %s\n' % unicode(self.url)
if self.response is not None:
res += """
REQUEST HEADERS
"""
res += """
NO REQUEST INFORMATION AVAILABLE
"""
for key, value in self.response.request.headers.iteritems():
if self.res_data is not None:
res += '%s: %s\n' % (key, value)
res += """
REQUEST DATA
%s
""" % self.response.request.body
headers = self.response.headers.items()
res += """
NO RESPONSE INFORMATION AVAILABLE
"""
res += """
RESPONSE HEADERS
%s""" % ''.join([('%s: %s\n' % (header[0],
    header[1])) for header in headers])
return res
res += """
RESPONSE DATA
%s
""" % self.res_data
