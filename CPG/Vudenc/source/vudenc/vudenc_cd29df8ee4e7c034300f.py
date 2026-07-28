"""
This file contains various controllers for table views.
The responsibility of the controller is to populate the table view with some data, contained in a specific model.
"""
from __future__ import absolute_import
from six import text_type
from TriblerGUI.tribler_request_manager import TriblerRequestManager
def sanitize_for_fts(text):...
return text_type(text).translate({ord(u'"'): u'""', ord(u"'"): u"''"})
