def _default_project(self, cr, uid, context={}):...
if 'project_id' in context and context['project_id']:
return context['project_id']
return False
