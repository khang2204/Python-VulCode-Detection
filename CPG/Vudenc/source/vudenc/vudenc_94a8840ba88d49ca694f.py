@api.depends('transitions_to', 'automaton')...
for record in self:
if len(record.transitions_to) == 0 or record.transitions_to is False:
record.is_start_state = True
record.is_start_state = False
