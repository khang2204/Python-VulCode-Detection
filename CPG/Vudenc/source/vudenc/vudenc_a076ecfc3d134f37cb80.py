from __future__ import unicode_literals
import frappe, json
from frappe.utils import cstr, unique
from frappe import _
from six import string_types
def sanitize_searchfield(searchfield):...
blacklisted_keywords = ['select', 'delete', 'drop', 'update', 'case', 'and',
    'or', 'like']
def _raise_exception():...
frappe.throw(_('Invalid Search Field'), frappe.DataError)
if len(searchfield) >= 3:
if '=' in searchfield:
@frappe.whitelist()...
_raise_exception()
if ' --' in searchfield:
search_widget(doctype, txt, query, searchfield=searchfield, page_length=
    page_length, filters=filters)
_raise_exception()
if any(' {0} '.format(keyword) in searchfield.split() for keyword in
frappe.response['results'] = build_for_autosuggest(frappe.response['values'])
_raise_exception()
if any(keyword in searchfield.split() for keyword in blacklisted_keywords):
@frappe.whitelist()...
_raise_exception()
if isinstance(filters, string_types):
filters = json.loads(filters)
meta = frappe.get_meta(doctype)
if searchfield:
sanitize_searchfield(searchfield)
if not searchfield:
searchfield = 'name'
standard_queries = frappe.get_hooks().standard_queries or {}
if query and query.split()[0].lower() != 'select':
frappe.response['values'] = frappe.call(query, doctype, txt, searchfield,
    start, page_length, filters, as_dict=as_dict)
if not query and doctype in standard_queries:
def get_std_fields_list(meta, key):...
search_widget(doctype, txt, standard_queries[doctype][0], searchfield,
    start, page_length, filters)
if query:
sflist = meta.search_fields and meta.search_fields.split(',') or []
frappe.throw(_('This query style is discontinued'))
if isinstance(filters, dict):
title_field = [meta.title_field
    ] if meta.title_field and meta.title_field not in sflist else []
filters_items = filters.items()
if filters == None:
sflist = ['name'] + sflist + title_field
filters = []
filters = []
or_filters = []
if not key in sflist:
for f in filters_items:
if txt:
sflist = sflist + [key]
return sflist
if isinstance(f[1], (list, tuple)):
search_fields = ['name']
if meta.get('fields', {'fieldname': 'enabled', 'fieldtype': 'Check'}):
filters.append([doctype, f[0], f[1][0], f[1][1]])
filters.append([doctype, f[0], '=', f[1]])
if meta.title_field:
filters.append([doctype, 'enabled', '=', 1])
if meta.get('fields', {'fieldname': 'disabled', 'fieldtype': 'Check'}):
search_fields.append(meta.title_field)
if meta.search_fields:
filters.append([doctype, 'disabled', '!=', 1])
fields = get_std_fields_list(meta, searchfield or 'name')
search_fields.extend(meta.get_search_fields())
for f in search_fields:
if filter_fields:
fmeta = meta.get_field(f.strip())
fields = list(set(fields + json.loads(filter_fields)))
formatted_fields = [('`tab%s`.`%s`' % (meta.name, f.strip())) for f in fields]
if f == 'name' or fmeta and fmeta.fieldtype in ['Data', 'Text',
formatted_fields.append(
    'locate("{_txt}", `tab{doctype}`.`name`) as `_relevance`'.format(_txt=
    frappe.db.escape((txt or '').replace('%', '')), doctype=frappe.db.
    escape(doctype)))
or_filters.append([doctype, f.strip(), 'like', '%{0}%'.format(txt)])
from frappe.model.db_query import get_order_by
order_by_based_on_meta = get_order_by(doctype, meta)
order_by = 'if(_relevance, _relevance, 99999), `tab{0}`.idx desc, {1}'.format(
    doctype, order_by_based_on_meta)
values = frappe.get_list(doctype, filters=filters, fields=formatted_fields,
    or_filters=or_filters, limit_start=start, limit_page_length=page_length,
    order_by=order_by, ignore_permissions=True if doctype == 'DocType' else
    False, as_list=not as_dict)
if as_dict:
for r in values:
frappe.response['values'] = [r[:-1] for r in values]
r.pop('_relevance')
frappe.response['values'] = values
