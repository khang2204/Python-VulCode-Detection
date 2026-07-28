def connect(addr, timeout):...
sock = create_client()
for _ in range(int(timeout * 10)):
return sock
sock.connect(addr)
if cls.VERBOSE:
print('+', end='')
time.sleep(0.1)
sys.stdout.flush()
