def _sanitize_content(self):...
"""docstring"""
if frappe.flags.in_install:
return
for fieldname, value in self.get_valid_dict().items():
if not value or not isinstance(value, string_types):
value = frappe.as_unicode(value)
if u'<' not in value and u'>' not in value:
if '<!-- markdown -->' in value and not ('<script' in value or 
df = self.meta.get_field(fieldname)
sanitized_value = value
if df and df.get('fieldtype') in ('Data', 'Code', 'Small Text') and df.get(
sanitized_value = sanitize_email(value)
if df and (df.get('ignore_xss_filter') or df.get('fieldtype') == 'Code' and
self.set(fieldname, sanitized_value)
sanitized_value = sanitize_html(value, linkify=df.fieldtype == 'Text Editor')
