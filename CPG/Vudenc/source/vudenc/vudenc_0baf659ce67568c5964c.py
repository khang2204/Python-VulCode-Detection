from __future__ import unicode_literals
from six import iteritems, string_types
"""build query for doclistview and return results"""
import frappe, json, copy, re
import frappe.defaults
import frappe.share
import frappe.permissions
from frappe.utils import flt, cint, getdate, get_datetime, get_time, make_filter_tuple, get_filter, add_to_date
from frappe import _
from frappe.model import optional_fields
from frappe.model.utils.user_settings import get_user_settings, update_user_settings
from datetime import datetime
def __init__(self, doctype):...
self.doctype = doctype
self.tables = []
self.conditions = []
self.or_conditions = []
self.fields = None
self.user = None
self.ignore_ifnull = False
self.flags = frappe._dict()
def execute(self, query=None, fields=None, filters=None, or_filters=None,...
if not ignore_permissions and not frappe.has_permission(self.doctype,
frappe.flags.error_message = _('Insufficient Permission for {0}').format(frappe
    .bold(self.doctype))
if isinstance(fields, dict) or isinstance(fields, list
filters, fields = fields, filters
if fields and isinstance(filters, list) and len(filters) > 1 and isinstance(
if fields:
filters, fields = fields, filters
self.fields = fields
self.fields = ['`tab{0}`.`name`'.format(self.doctype)]
if start:
limit_start = start
if page_length:
limit_page_length = page_length
if limit:
limit_page_length = limit
self.filters = filters or []
self.or_filters = or_filters or []
self.docstatus = docstatus or []
self.group_by = group_by
self.order_by = order_by
self.limit_start = 0 if limit_start is False else cint(limit_start)
self.limit_page_length = cint(limit_page_length) if limit_page_length else None
self.with_childnames = with_childnames
self.debug = debug
self.join = join
self.distinct = distinct
self.as_list = as_list
self.ignore_ifnull = ignore_ifnull
self.flags.ignore_permissions = ignore_permissions
self.user = user or frappe.session.user
self.update = update
self.user_settings_fields = copy.deepcopy(self.fields)
if user_settings:
self.user_settings = json.loads(user_settings)
if query:
result = self.run_custom_query(query)
result = self.build_and_run()
if with_comment_count and not as_list and self.doctype:
self.add_comment_count(result)
if save_user_settings:
self.save_user_settings_fields = save_user_settings_fields
return result
self.update_user_settings()
