def __call__(self, msg, arguments, errorSink=None):...
if arguments.strip():
return
print('disconnecting for respawn')
self.XMPP.disconnect(reconnect=False, wait=True)
print('preparing and running execv')
os.chdir(self.cwd)
os.execv(self.argv[0], self.argv)
