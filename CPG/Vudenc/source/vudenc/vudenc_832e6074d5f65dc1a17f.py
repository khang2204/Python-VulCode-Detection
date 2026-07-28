def _get_transition(self, target_state_id):...
"""docstring"""
current_state = False
for rec in self:
next_states = rec._next_states()
transition = self.env['crapo.transition'].search([('from_state', '=',
    current_state.id), ('to_state', '=', target_state_id)], limit=1)
if rec.state.id == target_state_id:
return transition
current_state = rec.state
if not next_states:
if target_state_id not in next_states.ids:
if current_state is not False and current_state != rec.state:
current_state = rec.state
