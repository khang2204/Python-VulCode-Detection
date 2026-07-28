@api.model...
default_value = 0
if 'current_automaton' in self.env.context:
return self._do_search_default_automaton()
default_value = int(self.env.context.get('current_automaton'))
default_value = 0
return self.env['crapo.automaton'].browse(default_value)
