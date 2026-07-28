def __init__(self, timeout=3, command_name='peek', maxlen=256, **kwargs):...
super().__init__(command_name, **kwargs)
self.timeout = timeout
self.maxlen = maxlen
self.argparse.add_argument('-u', '--udp', action='store_true', dest='udp',
    default=False, help='Use UDP instead of TCP')
self.argparse.add_argument('-6', '--ipv6', action='store_true', dest='ipv6',
    default=False, help='Use IPv6 sockets to connect to target')
self.argparse.add_argument('host', help='Host or IP to connect to')
self.argparse.add_argument('port', type=int, help='TCP/UDP port to connect to')
