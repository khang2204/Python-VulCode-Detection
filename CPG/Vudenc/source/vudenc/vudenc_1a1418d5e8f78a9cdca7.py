root = ['', 'home', 'root']
dirs = []
path = []
curr_path = [] or ['', 'home', 'root']
def mkdir():...
if dir in dirs:
print('Directory already exist.')
dirs.append(dir)
def ls():...
path.append(dir)
if path == root:
path = dirs
print(*path, sep='\n')
path = path[0]
def cd():...
if dir == '':
curr_path = root
if dir in dirs:
path = root
curr_path.append(dir)
if dir == '..':
def pwd():...
path.clear()
curr_path.pop()
print("Directory doesn't exist.")
print(*curr_path, sep='/')
print(*curr_path, sep='/')
def rm():...
i = len(dirs) - 1
if dir in dirs:
if dirs[i] in path:
dirs.remove(dir)
print('Directory does not exist.')
i = i - 1
path.append(dirs[i])
if dir in path:
def session_clear():...
path.pop()
path.remove(dir)
dirs.clear()
path.append(dirs[i])
curr_path.clear()
curr_path = root
path.clear()
def commands(argument):...
comm = {'mkdir': mkdir, 'ls': ls, 'cd': cd, 'pwd': pwd, 'rm': rm,
    'session_clear': session_clear, 'exit': exit}
if n in comm:
func = comm.get(argument)
print('command does not exist!')
func()
print(
    'There are total 7 commands: mkdir, ls, cd, pwd, rm, session_clear, exit.')
while True:
n = input('$: ')
a = []
a.append(n.split(' '))
n = a[0][0]
if n in ['mkdir', 'rm'] and len(a[0]) == 1:
print('{}:missing operand'.format(n))
if len(a[0]) == 1:
commands(n)
dir = ''
if len(a[0]) == 2:
dir = a[0][1]
print('Invalid Syntax')
