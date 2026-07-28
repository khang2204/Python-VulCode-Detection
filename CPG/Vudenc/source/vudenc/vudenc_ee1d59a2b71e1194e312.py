def _get_missing_mandatory_fields(self):...
"""docstring"""
def get_msg(df):...
if df.fieldtype == 'Table':
return '{}: {}: {}'.format(_('Error'), _('Data missing in table'), _(df.label))
if self.parentfield:
return '{}: {} {} #{}: {}: {}'.format(_('Error'), frappe.bold(_(self.
    doctype)), _('Row'), self.idx, _('Value missing for'), _(df.label))
return _('Error: Value missing for {0}: {1}').format(_(df.parent), _(df.label))
