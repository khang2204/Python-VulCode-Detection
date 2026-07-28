def string_col(col):...
col_type = ALL_COLUMNS.get(col, None)
col_type = str(col_type) if col_type else None
if col_type and 'String' in col_type and 'FixedString' not in col_type:
return escape_col(col)
return 'toString({})'.format(escape_col(col))
