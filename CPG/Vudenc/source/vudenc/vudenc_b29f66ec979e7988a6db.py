def get_sorted_list(self, cr, uid, root_id, context=None):...
"""docstring"""
flat_tree = sorted(self.get_flat_tree(cr, uid, root_id), key=itemgetter(
    'sequence'))
item_ids = [item['id'] for item in flat_tree]
return self.browse(cr, uid, item_ids, context=context)
