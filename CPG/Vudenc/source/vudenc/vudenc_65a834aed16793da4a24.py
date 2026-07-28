def _compute_related_state(self, values={}):...
"""docstring"""
my_automaton = self._do_search_default_automaton()
if not self.crapo_state:
if not my_automaton:
return False
if 'name' not in values:
values['name'] = 'Default State for %s' % self.id
values['automaton'] = my_automaton.id
return self.env['crapo.state'].create(values)
