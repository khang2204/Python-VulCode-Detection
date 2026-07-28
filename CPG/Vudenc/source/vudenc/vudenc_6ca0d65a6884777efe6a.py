"""
Pyjo.Path - Path
================
::

    import Pyjo.Path

    # Parse
    path = Pyjo.Path.new('/foo%2Fbar%3B/baz.html')
    print(path[0])

    # Build
    path = Pyjo.Path.new(u'/i/♥')
    path.append('pyjo')
    print(path)

:mod:`Pyjo.Path` is a container for paths used by :mod:`Pyjo.URL` and based on
:rfc:`3986`.
"""
import Pyjo.Base
import Pyjo.Mixin.String
from Pyjo.Util import b, u, url_escape, url_unescape
"""::

        path = Pyjo.Path.new()
        path = Pyjo.Path.new('/foo%2Fbar%3B/baz.html')

    Construct a new :mod`Pyjo.Path` object and :meth:`parse` path if necessary.
    """
charset = 'utf-8'
"""::

        charset = path.charset
        path.charset = 'utf-8'

    Charset used for encoding and decoding, defaults to ``utf-8``. ::

        # Disable encoding and decoding
        path.charset = None
    """
_leading_slash = False
_path = None
_parts = None
_trailing_slash = False
def __init__(self, path=None):...
super(Pyjo_Path, self).__init__()
if path is not None:
self.parse(path)
def __bool__(self):...
"""docstring"""
return True
