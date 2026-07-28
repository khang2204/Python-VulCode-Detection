@api.depends('state')...
for rec in self:
if rec.state.readonly_fields:
rec.crapo_readonly_fields = ',{},'.format(rec.state.readonly_fields)
rec.crapo_readonly_fields = ',0,'
