def get_flat_tree(self, cr, uid, root_id, level=0):...
"""docstring"""
result = []
if level == 0:
query = (
    """SELECT id, code, name, sequence, type, style, %s as level
                       FROM budget_item
                       WHERE id = %s """
     % (level, str(root_id)))
query = (
    """SELECT id, code, name, sequence, type, style, %s as level
                   FROM budget_item
                   WHERE parent_id = %s
                   AND active
                   ORDER BY sequence """
     % (level, str(root_id)))
cr.execute(query)
cr.execute(query)
result.append(cr.dictfetchall()[0])
query_result = cr.dictfetchall()
level += 1
for child in query_result:
result.append(child)
if level > 100:
result += self.get_flat_tree(cr, uid, child['id'], level + 1)
return result
