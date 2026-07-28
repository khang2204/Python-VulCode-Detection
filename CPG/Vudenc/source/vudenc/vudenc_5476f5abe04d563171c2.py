from __future__ import unicode_literals
from six import iteritems, string_types
import datetime
import frappe, sys
from frappe import _
from frappe.utils import cint, flt, now, cstr, strip_html, sanitize_html, sanitize_email, cast_fieldtype
from frappe.model import default_fields
from frappe.model.naming import set_new_name
from frappe.model.utils.link_count import notify_link_count
from frappe.modules import load_doctype_module
from frappe.model import display_fieldtypes
from frappe.model.db_schema import type_map, varchar_len
from frappe.utils.password import get_decrypted_password, set_encrypted_password
_classes = {}
def get_controller(doctype):...
"""docstring"""
from frappe.model.document import Document
if not doctype in _classes:
module_name, custom = frappe.db.get_value('DocType', doctype, ('module',
    'custom'), cache=True) or ['Core', False]
return _classes[doctype]
if custom:
_class = Document
module = load_doctype_module(doctype, module_name)
_classes[doctype] = _class
classname = doctype.replace(' ', '').replace('-', '')
if hasattr(module, classname):
_class = getattr(module, classname)
if issubclass(_class, BaseDocument):
_class = getattr(module, classname)
