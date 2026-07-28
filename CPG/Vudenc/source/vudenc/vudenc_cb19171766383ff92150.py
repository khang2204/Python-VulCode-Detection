def get_approvers(department):...
if not department:
return []
approvers = []
department_details = frappe.db.get_value('Department', {'name': department},
    ['lft', 'rgt'], as_dict=True)
department_list = frappe.db.sql(
    """select name from `tabDepartment`
		where lft >= %s and rgt <= %s order by lft desc
		"""
    , (department_details.lft, department_details.rgt), as_list=True)
for d in department_list:
approvers.extend([l.leave_approver for l in frappe.db.sql(
    "select approver from `tabDepartment Approver` \t\t\twhere parent = %s and parentfield = 'leave_approvers'"
    , d, as_dict=True)])
return approvers
