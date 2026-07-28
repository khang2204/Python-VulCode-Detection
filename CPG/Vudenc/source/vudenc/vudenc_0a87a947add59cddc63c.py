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
