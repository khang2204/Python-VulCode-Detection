"""Serve files directly from the ContentsManager."""
import mimetypes
import json
from base64 import decodebytes
from tornado import web
from notebook.base.handlers import IPythonHandler
from notebook.utils import maybe_future
"""serve files via ContentsManager

    Normally used when ContentsManager is not a FileContentsManager.

    FileContentsManager subclasses use AuthenticatedFilesHandler by default,
    a subclass of StaticFileHandler.
    """
@property...
return super(FilesHandler, self
    ).content_security_policy + '; sandbox allow-scripts'
