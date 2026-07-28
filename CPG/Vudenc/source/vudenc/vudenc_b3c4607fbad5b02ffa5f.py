def shell(self):...
"""docstring"""
cwd = self.fs_root
cuser = 'system'
cwd_list = ['']
while True:
cwd_fl = ''.join(i + '/' for i in cwd_list)
print('root@postgres %s$ ' % cwd_fl, end='')
cmd_input = input()
cmd = cmd_input.split(' ')
op = cmd[0]
if op == 'ls':
res = self.listdir(cwd)
if op == 'cat':
print('Owner       Upload Time         Size            Filename            ')
dest = self.locate(cmd[1], parent=cwd)
if op == 'cd':
print('--------------------------------------------------------------------')
print(self.get_content(dest))
if cmd[1] == '..':
if op == 'chown':
for item in res:
cwd_dest = cwd.parent
cwd_dest = cwd.sub_names_idx[cmd[1]]
dest = self.locate(cmd[1], parent=cwd)
if op == 'rename':
print('%s%s%s%s' % (item['owner'].ljust(12), str(int(item['upload-time'])).
    ljust(20), str(item['file-size'] if not item['is-dir'] else '').ljust(
    16), item['file-name']))
print('Total: %d' % len(res))
if cwd_dest:
if cwd_dest:
self.chown(dest, cmd[2])
dest = self.locate(cmd[1], parent=cwd)
if op == 'mkdir':
print('')
cwd = cwd_dest
cwd = cwd_dest
self.rename(dest, cmd[2])
self.mkdir(cwd, cmd[1], cuser)
if op == 'mkfile':
cwd_list = cwd_list[:-1]
cwd_list.append(cmd[1])
self.mkfile(cwd, cmd[1], cuser, b'')
if op == 'rm':
self.remove(self.locate(cmd[1], parent=cwd))
if op == 'cp':
src = self.locate(cmd[1], parent=cwd)
if op == 'mv':
self.copy(src, cmd[2])
src = self.locate(cmd[1], parent=cwd)
if op == 'q':
self.move(src, cmd[2])
print('Unknown command "%s".' % op)
return
