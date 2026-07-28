def get_data(filters, leave_types):...
user = frappe.session.user
allocation_records_based_on_to_date = get_leave_allocation_records(filters.
    to_date)
allocation_records_based_on_from_date = get_leave_allocation_records(filters
    .from_date)
active_employees = frappe.get_all('Employee', filters={'status': 'Active',
    'company': filters.company}, fields=['name', 'employee_name',
    'department', 'user_id'])
data = []
for employee in active_employees:
leave_approvers = get_approvers(employee.department)
return data
if len(leave_approvers) and user in leave_approvers or user in ['Administrator'
row = [employee.name, employee.employee_name, employee.department]
for leave_type in leave_types:
leaves_taken = get_approved_leaves_for_period(employee.name, leave_type,
    filters.from_date, filters.to_date)
data.append(row)
opening = get_leave_balance_on(employee.name, leave_type, filters.from_date,
    allocation_records_based_on_from_date.get(employee.name, frappe._dict()))
closing = get_leave_balance_on(employee.name, leave_type, filters.to_date,
    allocation_records_based_on_to_date.get(employee.name, frappe._dict()))
row += [opening, leaves_taken, closing]
