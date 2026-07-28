def _next_states(self):...
self.ensure_one()
domain = self._get_state_domain()
next_states = False
if self.automaton:
eligible_transitions = self.env['crapo.transition'].search([('automaton',
    '=', self.automaton.id), ('from_state', '=', self.state.id)])
domain.append(('sequence', '>', self.state.sequence))
target_ids = eligible_transitions.mapped(lambda x: x.to_state.id)
next_states = self.env['crapo.state'].search(domain, limit=1)
if target_ids:
return next_states
domain.append(('id', 'in', target_ids))
next_states = self.env['crapo.state'].search(domain)
