def get_table_definition(name, engine, columns=ALL_COLUMNS):...
return """
    CREATE TABLE IF NOT EXISTS %(name)s (%(columns)s) ENGINE = %(engine)s""" % {
    'columns': columns.for_schema(), 'engine': engine, 'name': name}
