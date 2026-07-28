def _do_search_default_automaton(self):...
"""docstring"""
automaton_model = self.env['crapo.automaton']
my_model = self.env['ir.model'].search([('model', '=', self.
    _state_for_model)], limit=1)
my_automaton = automaton_model.search([('model_id', '=', my_model.id)])
if not my_automaton:
my_automaton = automaton_model.create({'name': 'Automaton for {}'.format(
    self._state_for_model), 'model_id': my_model.id})
return my_automaton
