def newConnection(self):...
args = self._dbArgs.copy()
self.augmentDatabaseArgs(args)
return self.dbapiModule().connect(**args)
