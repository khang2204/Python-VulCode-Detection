def copy(self, cr, uid, id, default={}, context={}):...
proj = self.browse(cr, uid, id, context=context)
default = default or {}
context['active_test'] = False
default['state'] = 'open'
if not default.get('name', False):
default['name'] = proj.name + _(' (copy)')
res = super(project, self).copy(cr, uid, id, default, context)
ids = self.search(cr, uid, [('parent_id', 'child_of', [res])])
cr.execute('update project_task set active=True where project_id in %s',
    tuple(ids))
return res
