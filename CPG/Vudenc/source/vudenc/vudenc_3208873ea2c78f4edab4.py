def generate_select(self, queryInstance):...
target = '*'
joint = ''
if queryInstance._joins:
for join in queryInstance._joins:
where = ''
joint_type = join.joint_type
if queryInstance._where:
if joint_type == self.JOIN:
i = 0
end = ';'
joint_type = self.JOIN
joint_type = self.LEFT_JOIN
if isinstance(queryInstance._where, str):
if queryInstance._delete:
if join.dest in join.src._meta.rel_class and join.src.isForeignKey(join.src
where = 'WHERE {0}'.format(queryInstance._where)
where = queryInstance._where.parse()
queryType = 'DELETE'
queryType = 'SELECT {0}'.format(','.join(target))
clause1 = '%s.%s' % (join.src._meta.table_name, join.src._meta.rel_class[
    join.dest].name)
if join.src in join.dest._meta.rel_class and join.dest.isForeignKey(join.
where = 'WHERE {0}'.format(where)
if queryInstance.model_class._meta.primary_key:
query = '{0} FROM {1} {2} {3}{4}'.format(queryType, queryInstance.
    model_class._meta.table_name, joint, where, end)
clause2 = '%s.%s' % (join.dest._meta.table_name, join.src._meta.rel_class[
    join.dest].reference.name)
clause1 = '%s.%s' % (join.src._meta.table_name, join.dest._meta.rel_class[
    join.src].reference.name)
joint += '%s %s on (%s = %s) ' % (joint_type, join.dest._meta.table_name,
    clause1, clause2)
end = ' RETURNING id;'
return query
clause2 = '%s.%s' % (join.dest._meta.table_name, join.dest._meta.rel_class[
    join.src].name)
