def _extract_images_from_text_editor(self):...
from frappe.utils.file_manager import extract_images_from_doc
if self.doctype != 'DocType':
for df in self.meta.get('fields', {'fieldtype': ('=', 'Text Editor')}):
extract_images_from_doc(self, df.fieldname)
