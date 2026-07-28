def get_first_if(self):...
"""docstring"""
iface = ''
expected = 16
python_arc = platform.architecture()[0]
if python_arc == '64bit':
struct_size = 40
struct_size = 32
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
buff = array.array('B', b'\x00' * (expected * struct_size))
param = struct.pack('iL', expected * struct_size, buff.buffer_info()[0])
ret = fcntl.ioctl(sock.fileno(), 35090, param)
retsize = struct.unpack('iL', ret)[0]
if retsize == expected * struct_size:
logger.warn('SIOCGIFCONF returned more than {0} up network interfaces.',
    expected)
sock = buff.tostring()
for i in range(0, struct_size * expected, struct_size):
iface = self._format_single_interface_name(sock, i)
return iface.decode('latin-1'), socket.inet_ntoa(sock[i + 20:i + 24])
if b'lo' in iface:
