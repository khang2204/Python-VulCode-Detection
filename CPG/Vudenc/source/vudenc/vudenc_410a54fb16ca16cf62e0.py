def do_reopen(self, cr, uid, ids, *args):...
request = self.pool.get('res.request')
tasks = self.browse(cr, uid, ids)
for task in tasks:
project = task.project_id
return True
if project and project.warn_manager and project.manager.id and project.manager.id != uid:
request.create(cr, uid, {'name': _("Task '%s' set in progress") % task.name,
    'state': 'waiting', 'act_from': uid, 'act_to': project.manager.id,
    'ref_partner_id': task.partner_id.id, 'ref_doc1': 'project.task,%d' %
    task.id, 'ref_doc2': 'project.project,%d' % project.id})
self.write(cr, uid, [task.id], {'state': 'open'})
