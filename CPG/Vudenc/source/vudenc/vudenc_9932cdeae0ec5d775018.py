def __init__(self, app=None, credentials_store=None, http=None, time=None,...
self.credentials_store = (credentials_store if credentials_store is not
    None else MemoryCredentials())
self.http = http if http is not None else httplib2.Http()
self.time = time if time is not None else time_module.time
self.urandom = urandom if urandom is not None else os.urandom
if app is not None:
self.init_app(app)
