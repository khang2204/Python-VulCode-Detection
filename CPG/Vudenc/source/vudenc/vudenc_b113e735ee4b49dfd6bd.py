def formatCommand(e):...
if e.startswith('!'):
return e[1:]
return e.format(url=url, dest=dest.name)
