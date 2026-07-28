@api.model...
automaton_model = self.env['crapo.automaton']
my_model = self.env['ir.model'].search([('model', '=', self._name)], limit=1)
my_automaton = automaton_model.search([('model_id', '=', my_model.id)], limit=1
    )
if my_automaton:
return my_automaton
return automaton_model.create({'name': 'Automaton for {}'.format(self._name
    ), 'model_id': my_model.id})
