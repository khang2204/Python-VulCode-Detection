def __init__(self, count=4, interval=0.5, command_name='ping', **kwargs):...
super().__init__(command_name, **kwargs)
self.argparse.add_argument('-6', '--ipv6', action='store_true', dest='ipv6',
    default=False, help='Use ping6 instead of ping')
self.argparse.add_argument('--alot', action='store_true', dest='alot', help
    ='Send more pings')
self.argparse.add_argument('host', help='Host which is to be pinged')
self.pingargs = ['-q', '-i{0:f}'.format(interval)]
