def setActive(self, cr, uid, ids, value=True, context={}):...
for proj in self.browse(cr, uid, ids, context):
self.write(cr, uid, [proj.id], {'state': value and 'open' or 'template'},
    context)
return True
cr.execute('select id from project_task where project_id=%s', (proj.id,))
tasks_id = [x[0] for x in cr.fetchall()]
if tasks_id:
self.pool.get('project.task').write(cr, uid, tasks_id, {'active': value},
    context)
cr.execute('select id from project_project where parent_id=%s', (proj.id,))
project_ids = [x[0] for x in cr.fetchall()]
for child in project_ids:
self.setActive(cr, uid, [child], value, context)
