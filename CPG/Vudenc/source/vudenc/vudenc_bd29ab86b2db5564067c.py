def copy_data(self, cr, uid, id, default={}, context={}):...
default = default or {}
default['work_ids'] = []
return super(task, self).copy_data(cr, uid, id, default, context)
