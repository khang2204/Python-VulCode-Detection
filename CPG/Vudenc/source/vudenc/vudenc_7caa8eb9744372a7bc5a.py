def __prepare(self, sql, filename):...
if sql is None and filename is not None:
filename = Connection.path(filename, '.sql')
sql = re.sub('\\{(\\w+?)\\}', '%(\\1)s', sql)
logger.debug('READ SQL FILE: ' + filename)
return sql
sql = file.read()
