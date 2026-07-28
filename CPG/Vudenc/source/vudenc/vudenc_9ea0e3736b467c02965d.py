def _fetch_row_sql(root_ids):...
query = SQL_RECURSIVE_QUERY_EDUCATION_GROUP.format(list_root_ids=','.join(
    str(root_id) for root_id in root_ids))
cursor.execute(query)
return [{'id': row[0], 'child_branch_id': row[1], 'child_leaf_id': row[2],
    'parent_id': row[3], 'level': row[4]} for row in cursor.fetchall()]
