@classmethod...
if addr is None:
addr = cls.HOST, cls.PORT
conn = DebugSessionConnection.create_client(addr, timeout=kwargs.get('timeout')
    )
return cls(conn, owned=True, **kwargs)
