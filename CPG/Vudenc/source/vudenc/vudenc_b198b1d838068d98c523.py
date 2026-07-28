def do_close(self, cr, uid, ids, *args):...
request = self.pool.get('res.request')
tasks = self.browse(cr, uid, ids)
for task in tasks:
project = task.project_id
return True
if project:
if project.warn_manager and project.manager and project.manager.id != uid:
self.write(cr, uid, [task.id], {'state': 'done', 'date_close': time.
    strftime('%Y-%m-%d %H:%M:%S'), 'remaining_hours': 0.0})
request.create(cr, uid, {'name': _("Task '%s' closed") % task.name, 'state':
    'waiting', 'act_from': uid, 'act_to': project.manager.id,
    'ref_partner_id': task.partner_id.id, 'ref_doc1': 'project.task,%d' % (
    task.id,), 'ref_doc2': 'project.project,%d' % (project.id,)})
if task.parent_id and task.parent_id.state in ('pending', 'draft'):
reopen = True
for child in task.parent_id.child_ids:
if child.id != task.id and child.state not in ('done', 'cancelled'):
if reopen:
reopen = False
self.do_reopen(cr, uid, [task.parent_id.id])
