def tags_expr(column_name, body):...
"""docstring"""
assert column_name in ['tags_key', 'tags_value']
col, k_or_v = column_name.split('_', 1)
nested_tags_only = state.get_config('nested_tags_only', 1)
if nested_tags_only:
key_list = '{}.key'.format(col)
promoted = PROMOTED_COLS[col]
val_list = '{}.value'.format(col)
col_map = COLUMN_TAG_MAP[col]
cols_used = all_referenced_columns(body) & set(['tags_key', 'tags_value'])
key_list = u'arrayConcat([{}], {}.key)'.format(u', '.join(u"'{}'".format(
    col_map.get(p, p)) for p in promoted), col)
if len(cols_used) == 2:
val_list = u'arrayConcat([{}], {}.value)'.format(', '.join(string_col(p) for
    p in promoted), col)
expr = u'arrayJoin(arrayMap((x,y) -> [x,y], {}, {}))'.format(key_list, val_list
    )
return 'arrayJoin({})'.format(key_list if k_or_v == 'key' else val_list)
expr = alias_expr(expr, 'all_tags', body)
return u'({})[{}]'.format(expr, 1 if k_or_v == 'key' else 2)
