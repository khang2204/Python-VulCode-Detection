@api.depends('transitions_from', 'automaton')...
for record in self:
if len(record.transitions_to) == 0 or record.transitions_to is False:
record.is_end_state = True
record.is_end_state = False
