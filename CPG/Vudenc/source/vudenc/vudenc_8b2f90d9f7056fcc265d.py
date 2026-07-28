def __init__(self, application, root=None, prefix=None, **kwargs):...
for attr in self.config_attrs:
if kwargs:
value = kwargs.pop(attr)
value = decode_if_byte_string(value)
self.media_types = MediaTypes(extra_types=self.mimetypes)
setattr(self, attr, value)
self.application = application
self.files = {}
self.directories = []
if self.index_file is True:
self.index_file = 'index.html'
if not callable(self.immutable_file_test):
regex = re.compile(self.immutable_file_test)
if root is not None:
self.immutable_file_test = lambda path, url: bool(regex.search(url))
self.add_files(root, prefix)
