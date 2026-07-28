def get_sub_items(self, cr, item_ids):...
"""docstring"""
parents_ids = item_ids
items_ids = copy.copy(parents_ids)
loop_counter = 0
while len(parents_ids) > 0:
query = (
    """SELECT id
                       FROM budget_item
                       WHERE parent_id IN ( %s )
                       AND active """
     % ','.join(map(str, parents_ids)))
return list(set(item_ids))
cr.execute(query)
children_ids = map(lambda x: x[0], cr.fetchall())
items_ids += children_ids
parents_ids = copy.copy(children_ids)
loop_counter += 1
if loop_counter > 100:
