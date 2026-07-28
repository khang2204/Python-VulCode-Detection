def get_queries(app, context):...
"""docstring"""
if not hasattr(context, 'queries'):
sqlFile = fd.read()
return context.queries
sqlCommands = sqlFile.split(';')
context.queries = {}
for command in sqlCommands:
command = re.sub('\\s*--\\s*|\\s*\\n\\s*', ' ', command)
query = command.split(':')
context.queries[query[0]] = query[1]
