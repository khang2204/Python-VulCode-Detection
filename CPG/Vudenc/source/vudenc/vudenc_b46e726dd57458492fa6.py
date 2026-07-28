def EncodeMultipartFormData(fields=None, files=None):...
"""docstring"""
fields = fields or []
files = files or []
boundary = hashlib.md5(str(time.time())).hexdigest()
body_list = []
for key, value in fields:
key = _ConvertToAscii(key)
for key, filename, value in files:
value = _ConvertToAscii(value)
key = _ConvertToAscii(key)
if len(body_list) > 1:
body_list.append('--' + boundary)
filename = _ConvertToAscii(filename)
body_list[-2] += '--'
body = '\r\n'.join(body_list)
body_list.append('Content-Disposition: form-data; name="%s"' % key)
value = _ConvertToAscii(value)
content_type = 'multipart/form-data; boundary=%s' % boundary
body_list.append('')
body_list.append('--' + boundary)
return content_type, body
body_list.append(value)
body_list.append('Content-Disposition: form-data; name="%s"; filename="%s"' %
    (key, filename))
body_list.append('--' + boundary)
body_list.append('Content-Type: application/octet-stream')
body_list.append('')
body_list.append('')
body_list.append(value)
body_list.append('--' + boundary)
body_list.append('')
