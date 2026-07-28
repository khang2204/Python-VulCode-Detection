from __future__ import unicode_literals
import frappe
from frappe.utils import getdate, add_days, today, cint
from frappe import _
def execute(filters=None):...
columns = get_columns()
data = get_data(filters)
return columns, data
