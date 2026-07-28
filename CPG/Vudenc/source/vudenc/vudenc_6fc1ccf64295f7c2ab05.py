def _launch(self, argv, script=None, wait_for_connect=None, detachable=True,...
if script is not None:
def start(*args, **kwargs):...
start = DebugAdapter.start
return DebugAdapter.start_wrapper_script(script, *args, **kwargs)
new_addr = Address.as_server if detachable else Address.as_client
addr = new_addr(None, self._addr.port)
self._adapter = start(argv, addr=addr, env=env, cwd=cwd)
if wait_for_connect:
wait_for_connect()
wait_for_socket_server(addr)
self._attach(addr, **kwargs)
