@classmethod...
if addr is None:
addr = cls.HOST, cls.PORT
conn = DebugSessionConnection.create_server(addr, **kwargs)
return cls(conn, owned=True, **kwargs)
