def registerPlayer(name):...
"""docstring"""
name = bleach.clean(name)
execute('insert into Player(name) values(%s)', (name,))
