def _handle_string(self, submit, tmppath, line):...
if not line:
return
if validate_hash(line):
if validate_url(line):
filedata = VirusTotalAPI().hash_fetch(line)
submit['errors'].append('Error retrieving file hash: %s' % e)
filepath = Files.create(tmppath, line, filedata)
submit['data'].append({'type': 'url', 'data': line})
submit['errors'].append("'%s' was neither a valid hash or url" % line)
return
submit['data'].append({'type': 'file', 'data': filepath})
return
return
