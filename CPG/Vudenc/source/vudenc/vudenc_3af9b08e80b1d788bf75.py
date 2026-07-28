def execute(command):...
clients = find_repositories(command.path)
if command.repos:
ordered_clients = dict((client.path, client) for client in clients)
jobs = {}
for k in sorted(ordered_clients.keys()):
for client in clients:
client = ordered_clients[k]
cmd = command.get_command_line(client)
wait_for = jobs.keys()
print('%s (%s)' % (k, client.type))
job = {'client': client, 'cmd': cmd}
while wait_for:
if not cmd:
if len(jobs) > 1:
pid, retcode = os.wait()
pid, retcode = os.waitpid(wait_for[0], 0)
if pid in wait_for:
cmd = ['echo', '"%s" is not implemented for client "%s"' % (command.
    __class__.__name__, client.type)]
if command.debug:
print('')
path_to_pid = {job['client'].path: pid for pid, job in jobs.items()}
wait_for.remove(pid)
print('Executing shell command "%s" in "%s"' % (' '.join(cmd), client.path))
p = subprocess.Popen(cmd, shell=False, cwd=os.path.abspath(client.path),
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
pids_in_order = [path_to_pid[path] for path in sorted(path_to_pid.keys())]
job = jobs[pid]
job['process'] = p
for pid in pids_in_order:
job['retcode'] = retcode
jobs[p.pid] = job
job = jobs[pid]
job['stdout'] = job['process'].stdout.read()
client = job['client']
if len(jobs) > 1:
print(ansi('bluef') + '=== ' + ansi('boldon') + client.path + ansi(
    'boldoff') + ' (' + client.type + ') ===' + ansi('reset'))
if job['cmd']:
output = job['stdout'].rstrip()
if retcode == 0:
sys.stdout.write('s')
if job['retcode'] != 0:
sys.stdout.write('.')
sys.stdout.write('E')
sys.stdout.flush()
if not output:
if not job['cmd']:
output = 'Failed with retcode %d' % job['retcode']
output = ansi('redf') + output + ansi('reset')
output = ansi('yellowf') + output + ansi('reset')
if output:
print(output)
