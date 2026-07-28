def do_cancel(self, cr, uid, ids, *args):...
request = self.pool.get('res.request')
tasks = self.browse(cr, uid, ids)
for task in tasks:
project = task.project_id
return True
if project.warn_manager and project.manager and project.manager.id != uid:
request.create(cr, uid, {'name': _("Task '%s' cancelled") % task.name,
    'state': 'waiting', 'act_from': uid, 'act_to': project.manager.id,
    'ref_partner_id': task.partner_id.id, 'ref_doc1': 'project.task,%d' %
    task.id, 'ref_doc2': 'project.project,%d' % project.id})
self.write(cr, uid, [task.id], {'state': 'cancelled', 'remaining_hours': 0.0})
