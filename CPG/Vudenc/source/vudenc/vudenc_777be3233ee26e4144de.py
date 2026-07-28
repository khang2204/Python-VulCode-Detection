def _get_state_domain(self, domain=None):...
result = []
if self.automaton:
result.append(('automaton', '=', self.automaton.id))
result.append(('automaton', '=', self._get_model_automaton().id))
return result
