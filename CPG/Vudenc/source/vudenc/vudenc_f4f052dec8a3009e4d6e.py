"""
Views and functions for serving static files. These are only to be used
during development, and SHOULD NOT be used in a production setting.
"""
import mimetypes
import os
import posixpath
import re
import stat
from django.http import FileResponse, Http404, HttpResponse, HttpResponseNotModified, HttpResponseRedirect
from django.template import Context, Engine, TemplateDoesNotExist, loader
from django.utils.http import http_date, parse_http_date
from django.utils.translation import gettext as _, gettext_lazy
def serve(request, path, document_root=None, show_indexes=False):...
"""docstring"""
path = posixpath.normpath(path)
path = path.lstrip('/')
newpath = ''
for part in path.split('/'):
if not part:
if newpath and path != newpath:
drive, part = os.path.splitdrive(part)
return HttpResponseRedirect(newpath)
fullpath = os.path.join(document_root, newpath)
head, part = os.path.split(part)
if os.path.isdir(fullpath):
if part in (os.curdir, os.pardir):
if show_indexes:
if not os.path.exists(fullpath):
newpath = os.path.join(newpath, part).replace('\\', '/')
return directory_index(newpath, fullpath)
statobj = os.stat(fullpath)
if not was_modified_since(request.META.get('HTTP_IF_MODIFIED_SINCE'),
return HttpResponseNotModified()
content_type, encoding = mimetypes.guess_type(fullpath)
content_type = content_type or 'application/octet-stream'
response = FileResponse(open(fullpath, 'rb'), content_type=content_type)
response['Last-Modified'] = http_date(statobj.st_mtime)
if stat.S_ISREG(statobj.st_mode):
response['Content-Length'] = statobj.st_size
if encoding:
response['Content-Encoding'] = encoding
return response
