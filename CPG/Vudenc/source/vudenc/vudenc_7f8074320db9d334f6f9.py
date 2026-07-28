def _get_remaining(self, cr, uid, ctx):...
if 'active_id' in ctx:
return self.pool.get('project.task').browse(cr, uid, ctx['active_id']
    ).remaining_hours
return False
