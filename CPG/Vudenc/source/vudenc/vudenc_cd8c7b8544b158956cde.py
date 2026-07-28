def replace(self, table, dataframe, batch_size=None):...
import migrate.changeset
suffix = datetime.now().strftime('_%Y%m%d%H%M%S').encode('utf-8')
self.metadata
temp = 'tmp_'.encode('utf-8')
source = sqlalchemy.Table(table, self.metadata, autoload=True,
    autoload_with=self._engine)
destination_name = 'tmp_' + hashlib.sha256(temp + table.encode('utf-8') +
    suffix).hexdigest()[0:56]
destination = sqlalchemy.Table(destination_name, self.metadata, autoload=False)
for column in source.columns:
destination.append_column(column.copy())
destination.create()
original_names = {}
for index in source.indexes:
name = hashlib.sha256(temp + index.name.encode('utf-8') + suffix).hexdigest()[
    0:60]
self.insert(destination.name, dataframe, batch_size=batch_size)
original_names[name] = index.name
self.execute(
    "BEGIN; SET LOCAL statement_timeout = '1min'; ANALYZE %s; COMMIT;" % table)
columns = []
backup = sqlalchemy.Table(table + '_b', self.metadata)
for column in index.columns:
backup.drop(bind=self._connection, checkfirst=True)
columns.append(next(x for x in destination.columns if x.name == column.name))
new = sqlalchemy.Index(name, *columns)
source.rename(name=source.name + '_b', connection=self._connection)
new.unique = index.unique
destination.rename(name=table, connection=self._connection)
new.table = destination
for index in source.indexes:
new.create(bind=self._connection)
index.rename(index.name[0:-2] + '_b', connection=self._connection)
for index in destination.indexes:
index.rename(original_names[index.name], connection=self._connection)
for func in _after_replace_callbacks:
func(destination, source)
