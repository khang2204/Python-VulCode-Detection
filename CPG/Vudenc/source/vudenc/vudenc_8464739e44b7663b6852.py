def get_if_mac(self, ifname):...
data = self._get_net_info()
if data[0] == ifname:
return data[2].replace(':', '').upper()
return None
