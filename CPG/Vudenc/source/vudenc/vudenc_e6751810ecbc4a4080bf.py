def clientthread(conn):...
sys.path.append(PLUGINPATH)
conn.send(output(hello()))
while True:
data = conn.recv(4096)
command = data.decode(ENCODING)
regex = re.compile('[^\\s]+(\\s[^\\s]+)?')
extractedCommand = regex.match(command).group()
print('#' + extractedCommand + '#')
if extractedCommand == 'nodes':
conn.send(output(nodes()))
if extractedCommand == 'help':
if not data:
conn.send(output(unknown()))
if extractedCommand == 'version':
sys.exit(5)
conn.send(output(version()))
if extractedCommand == 'cap':
conn.send(output(cap()))
if extractedCommand == 'list' or extractedCommand.startswith('list '):
conn.send(output(plugins()))
if extractedCommand == 'quit':
if extractedCommand.startswith('fetch '):
conn.close()
parts = extractedCommand.split(' ')
if extractedCommand.startswith('config '):
conn.send(output(runPlugin(parts[1])))
parts = extractedCommand.split(' ')
conn.send(output(unknown()))
conn.send(output(configPlugin(parts[1])))
