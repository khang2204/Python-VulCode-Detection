import os
from posixpath import normpath
import re
import warnings
from wsgiref.headers import Headers
from wsgiref.util import FileWrapper
from .media_types import MediaTypes
from .scantree import scantree
from .responders import StaticFile, MissingFileError, IsDirectoryError, Redirect
from .string_utils import decode_if_byte_string, decode_path_info, ensure_leading_trailing_slash
FOREVER = 10 * 365 * 24 * 60 * 60
config_attrs = ('autorefresh', 'max_age', 'allow_all_origins', 'charset',
    'mimetypes', 'add_headers_function', 'index_file', 'immutable_file_test')
autorefresh = False
max_age = 60
allow_all_origins = True
charset = 'utf-8'
mimetypes = None
add_headers_function = None
index_file = None
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
def __call__(self, environ, start_response):...
path = decode_path_info(environ.get('PATH_INFO', ''))
if self.autorefresh:
static_file = self.find_file(path)
static_file = self.files.get(path)
if static_file is None:
return self.application(environ, start_response)
return self.serve(static_file, environ, start_response)
