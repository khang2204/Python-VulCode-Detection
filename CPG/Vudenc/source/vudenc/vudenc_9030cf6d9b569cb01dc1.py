from __future__ import unicode_literals
import frappe
from frappe import _
from erpnext.hr.doctype.leave_application.leave_application import get_leave_allocation_records, get_leave_balance_on, get_approved_leaves_for_period
def execute(filters=None):...
leave_types = frappe.db.sql_list(
    'select name from `tabLeave Type` order by name asc')
columns = get_columns(leave_types)
data = get_data(filters, leave_types)
return columns, data
