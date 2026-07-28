def get_upload(self):...
"""docstring"""
if self.upload:
return self.upload
upload_key = self.request.get('upload_key')
if not upload_key:
return None
blob_info = storage.GcsBlobInfo.from_key(upload_key)
if not blob_info:
self.upload = blob_info
return self.upload
