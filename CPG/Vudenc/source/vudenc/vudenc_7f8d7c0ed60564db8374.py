@query_cached...
key = hashlib.sha1(str(sql).encode('utf-8')).hexdigest()
match = re.match('.*?select\\s(.*)from.*', sql, flags=re.IGNORECASE | re.
    UNICODE | re.DOTALL)
if match:
columns = []
columns = []
nested = 0
logger.warning(
    'Redshift unload requires poorly parsing column names from sql, found: {}'
    .format(columns))
potential = match[1].split(',')
sql = "UNLOAD ('" + sql.replace('\\', '\\\\').replace("'", "\\'") + "') "
for column in potential:
sql += "TO 's3://" + os.path.join(lore.io.bucket.name, self.UNLOAD_PREFIX,
    key, '') + "' "
nested += column.count('(')
if Connection.IAM_ROLE:
nested -= column.count(')')
sql += "IAM_ROLE '" + Connection.IAM_ROLE + "' "
sql += "DELIMITER '|' ADDQUOTES GZIP ALLOWOVERWRITE"
if nested == 0:
if re.match('(.*?)(limit\\s+\\d+)(.*)', sql, re.IGNORECASE | re.UNICODE |
columns.append(column.split()[-1].split('.')[-1].strip())
if column == potential[-1]:
logger.warning('LIMIT clause is not supported by unload, returning full set.')
self.__execute(sql, bindings)
column = re.split('from', column, flags=re.IGNORECASE)[0].strip()
sql = re.sub('(.*?)(limit\\s+\\d+)(.*)', '\\1\\3', sql, flags=re.IGNORECASE |
    re.UNICODE | re.DOTALL)
return key, columns
columns.append(column.split()[-1].split('.')[-1].strip())
