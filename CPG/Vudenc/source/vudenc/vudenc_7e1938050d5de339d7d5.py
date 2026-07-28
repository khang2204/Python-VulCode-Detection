def get_uploaded_file(self):...
uploaded_file = self.request.body
if not isinstance(uploaded_file, dict) or len(uploaded_file.keys()) != 5:
for filekey in uploaded_file.keys():
if filekey not in [u'body', u'body_len', u'content_type', u'filename',
return uploaded_file
