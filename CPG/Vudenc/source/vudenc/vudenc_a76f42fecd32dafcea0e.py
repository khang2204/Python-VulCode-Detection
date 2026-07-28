def topn_sum_graph(self, field, sum_by, limit=10):...
db = self.db
self.schema.limit = limit
FLOWS_PER_IP = self.schema.topn_sum(field, sum_by)
cursor = db.cursor()
cursor.execute('USE testgoflow')
cursor.execute(FLOWS_PER_IP)
r = cursor.fetchall()
g = Graph()
g.name = 'TopN {0}'.format(field)
g.set_headers([field, 'Total'])
g.graph_from_rows(r, 0)
return g
