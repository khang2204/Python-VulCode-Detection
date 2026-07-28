def do_login(self, ip_address=None, change_prompt=False, simics=False):...
self.write('\n')
self.read_until(boot=True)
if change_prompt:
self.write('export PS1="DrSEUs# "\n')
self.command('mkdir ~/.ssh')
self.read_until('export PS1="DrSEUs# "')
self.command('touch ~/.ssh/authorized_keys')
self.prompt = 'DrSEUs# '
self.command('echo "ssh-rsa ' + self.rsakey.get_base64() +
    '" > ~/.ssh/authorized_keys')
self.read_until()
if ip_address is None:
attempts = 10
self.command('ip addr add ' + ip_address + '/24 dev eth0')
for attempt in range(attempts):
self.command('ip link set eth0 up')
for line in self.command('ip addr show').split('\n'):
if simics:
self.command('ip addr show')
line = line.strip().split()
if ip_address is not None:
self.ip_address = '127.0.0.1'
self.ip_address = ip_address
if len(line) > 0 and line[0] == 'inet':
addr = line[1].split('/')[0]
if addr != '127.0.0.1':
ip_address = addr
