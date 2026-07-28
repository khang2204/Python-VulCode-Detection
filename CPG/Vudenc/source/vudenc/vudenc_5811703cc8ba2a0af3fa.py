def _include(self, env, _name=None, **kwargs):...
from core.models import Template
template_to_import = Template.get(Template.blog == self._tags.get('blog',
    None), Template.title == _name)
tpl = MetalTemplate(template_to_import.body, tags=self._tags)
self.includes.append(_name)
return tpl.execute(env['_stdout'], env)
