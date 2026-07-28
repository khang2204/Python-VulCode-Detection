def render(self, template_name, **template_vars):...
"""docstring"""
def get_vars():...
"""docstring"""
template_vars['env'] = self.env
template_vars['config'] = self.env.config
template_vars['params'] = self.params
return template_vars
