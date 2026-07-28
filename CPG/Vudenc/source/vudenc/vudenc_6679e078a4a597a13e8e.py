def newConnection(self):...
kwargs = self._dbArgs.copy()
self.augmentDatabaseArgs(kwargs)
return self.dbapiModule().connect(**kwargs)
