@event.listens_for(Engine, 'before_cursor_execute', retval=True)...
conn.info.setdefault('query_start_time', []).append(datetime.now())
stack = inspect.stack()[1:-1]
if sys.version_info.major == 3:
stack = [(x.filename, x.lineno, x.function) for x in stack]
stack = [(x[1], x[2], x[3]) for x in stack]
paths = [x[0] for x in stack]
origin = next((x for x in paths if lore.env.project in x), None)
if origin is None:
origin = next((x for x in paths if 'sqlalchemy' not in x), None)
if origin is None:
origin = paths[0]
caller = next(x for x in stack if x[0] == origin)
statement = '/* %s | %s:%d in %s */\n' % (lore.env.project, caller[0],
    caller[1], caller[2]) + statement
logger.debug(statement)
return statement, parameters
