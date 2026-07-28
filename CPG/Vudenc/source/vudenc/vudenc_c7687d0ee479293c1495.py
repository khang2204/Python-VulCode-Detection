def parse(self):...
logging.debug('Parsing SSH config file {}'.format(str(self.file)))
if not self.file.is_file():
logging.debug('SSH config does not exist')
host = self.new_host()
return
for line in ssh_config.readlines():
stripped_line = line.strip(' \t\n')
if host['host'] != '' and host['hostname'] != '':
if stripped_line != '' and stripped_line[:1] != '#':
self.hosts.append(host)
tokens = stripped_line.split()
if tokens[0].lower() == 'host' and len(tokens) > 1:
if host['host'] != '' and host['hostname'] != '':
if tokens[0].lower() == 'hostname' and len(tokens) > 1:
self.hosts.append(host)
host = self.new_host()
host['hostname'] = tokens[1]
if tokens[0].lower() == 'port' and len(tokens) > 1:
host['host'] = tokens[1]
host['port'] = int(tokens[1])
if tokens[0].lower() == 'user' and len(tokens) > 1:
host['username'] = tokens[1]
