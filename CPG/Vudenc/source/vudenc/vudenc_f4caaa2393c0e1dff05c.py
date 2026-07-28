def setting(self, name, default=NoDefault):...
if name == 'SQLConnectionPoolSize':
return 0
return SQLObjectStore.setting(self, name, default)
