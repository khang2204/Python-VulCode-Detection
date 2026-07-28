def tag_expr(column_name):...
"""docstring"""
col, tag = NESTED_COL_EXPR_RE.match(column_name).group(1, 2)
if col in PROMOTED_COLS:
actual_tag = TAG_COLUMN_MAP[col].get(tag, tag)
return u'{col}.value[indexOf({col}.key, {tag})]'.format(**{'col': col,
    'tag': escape_literal(tag)})
if actual_tag in PROMOTED_COLS[col]:
return string_col(actual_tag)
