def compute_hours(self, cr, uid, ids, context=None):...
if 'active_id' in context:
remaining_hrs = self.browse(cr, uid, ids)[0].remaining_hours
return {'type': 'ir.actions.act_window_close'}
self.pool.get('project.task').write(cr, uid, context['active_id'], {
    'remaining_hours': remaining_hrs})
