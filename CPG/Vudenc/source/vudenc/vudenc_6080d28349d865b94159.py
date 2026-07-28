def create_where(self, where):...
sql = 'WHERE '
lucene_parser = LuceneParser()
where_tuples = lucene_parser.parse(where)
for tuple in where_tuples:
sql += '{} {} {}'.format(tuple[0], tuple[1], tuple[2])
return sql
