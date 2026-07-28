def execute(filters=None):...
leave_types = frappe.db.sql_list(
    'select name from `tabLeave Type` order by name asc')
columns = get_columns(leave_types)
data = get_data(filters, leave_types)
return columns, data
