def commands(argument):...
comm = {'mkdir': mkdir, 'ls': ls, 'cd': cd, 'pwd': pwd, 'rm': rm,
    'session_clear': session_clear, 'exit': exit}
if n in comm:
func = comm.get(argument)
print('command does not exist!')
func()
