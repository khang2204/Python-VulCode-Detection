def __init__(self, command_name='dig', **kwargs):...
super().__init__(command_name, **kwargs)
self.argparse.add_argument('-s', '--server', '--at', default=None, help=
    'Server to ask for the record', dest='at')
self.argparse.add_argument('kind', metavar='RECTYPE', nargs='?', default=
    None, type=lambda x: x.upper(), choices=['SRV', 'A', 'AAAA', 'CNAME',
    'MX', 'SOA', 'TXT', 'SPF', 'NS', 'SSHFP', 'NSEC', 'NSEC3', 'DNSKEY',
    'RRSIG', 'DS', 'TLSA', 'PTR'], help='Record kind to ask for')
self.argparse.add_argument('name', metavar='NAME', help=
    'Record name to look up')
