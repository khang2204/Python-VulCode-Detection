def __init__(self):...
self.limit = 10
self.column_order = ['last_switched', 'src_ip', 'src_port', 'dst_ip',
    'dst_port', 'in_bytes']
src_ip_col = IP4Column('src_ip', 'Source IP')
src_ipv6_col = IP6Column('src_ipv6', 'Source IPv6')
dst_ip_col = IP4Column('dst_ip', 'Destination IP')
dst_ipv6_col = IP6Column('dst_ipv6', 'DestinationIPv6')
self.columns = {'last_switched': Column('last_switched', 'Last Switched'),
    'src_ip': Coalesce('src_c_ip', [src_ip_col, src_ipv6_col], src_ip_col.
    filter, 'Source IP'), 'src_port': PortColumn('src_port', 'Source Port'),
    'dst_ip': Coalesce('dst_c_ip', [dst_ip_col, dst_ipv6_col], dst_ip_col.
    filter, 'Destination IP'), 'dst_port': PortColumn('dst_port',
    'Destination Port'), 'in_bytes': IntColumn('in_bytes', 'Input bytes'),
    'in_pkts': IntColumn('in_pkts', 'Input Packets')}
self.QUERIES = {'TOPN': self.topn}
self.filters = []
self.filter_map = {'(\\d+\\-\\d+\\-\\d+)': 'last_switched',
    'src (\\d+\\.\\d+\\.\\d+\\.\\d+\\/\\d+|\\d+\\.\\d+\\.\\d+\\.\\d+)':
    'src_ip',
    'dst (\\d+\\.\\d+\\.\\d+\\.\\d+\\/\\d+|\\d+\\.\\d+\\.\\d+\\.\\d+)':
    'dst_ip', 'src ([0-9]+)($|\\s)': 'src_port', 'dst ([0-9]+)($|\\s)':
    'dst_port'}
