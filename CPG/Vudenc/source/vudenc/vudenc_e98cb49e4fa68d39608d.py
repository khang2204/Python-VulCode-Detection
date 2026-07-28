def test_port(port):...
s = socket.socket()
return s.connect_ex(('127.0.0.1', port)) == 0
s.close()
