def get_columns(leave_types):...
columns = [_('Employee') + ':Link/Employee:150', _('Employee Name') +
    '::200', _('Department') + '::150']
for leave_type in leave_types:
columns.append(_(leave_type) + ' ' + _('Opening') + ':Float:160')
return columns
columns.append(_(leave_type) + ' ' + _('Taken') + ':Float:160')
columns.append(_(leave_type) + ' ' + _('Balance') + ':Float:160')
