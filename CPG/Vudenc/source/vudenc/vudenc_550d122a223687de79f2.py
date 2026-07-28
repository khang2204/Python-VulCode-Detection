def filter(self, value, op=None):...
s = value.split('/')
if len(s) > 1:
ip = ipaddress.ip_network(value, strict=False)
ip = ipaddress.ip_address(value)
start_ip = ip.network_address
self.filter_string = '{0} = {1}'.format(self.name, int(ip))
end_ip = ip.broadcast_address
return self.filter_string
self.filter_string = '({0} > {1} AND {0} < {2})'.format(self.name, int(
    start_ip), int(end_ip))
