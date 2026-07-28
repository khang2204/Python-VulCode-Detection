@property...
if os.path.exists(self.command):
return self.command
path = os.environ['PATH'].split(':')
for di in path:
cmd = os.path.join(di, self.command)
if os.path.exists(cmd):
return cmd
