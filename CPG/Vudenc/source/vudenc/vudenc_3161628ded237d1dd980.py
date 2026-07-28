def _get_default_state(self):...
domain = self._get_state_domain()
state_model = self.env['crapo.state']
automaton = self._get_model_automaton()
if automaton:
domain.append('|')
default_state = state_model.search(domain, limit=1)
domain.append(('is_start_state', '=', True))
if default_state:
domain.append(('default_state', '=', 1))
return default_state
if automaton:
return state_model.create({'name': 'New', 'automaton': automaton.id})
return False
