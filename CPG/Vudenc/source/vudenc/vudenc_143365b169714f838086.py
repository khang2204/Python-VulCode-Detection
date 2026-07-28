@api.multi...
"""docstring"""
if 'default_state' in values:
if values['default_state']:
return super(State, self).write(values)
if len(self) > 1:
found = self.search([('default_state', '=', True), ('automaton', '=', self.
    automaton.id), ('id', '!=', self.id)])
for s in found:
s.write({'default_state': False})
