def do_setup(self, context):...
self.common = self._init_common()
self._check_flags()
self.iscsi_ips = {}
temp_iscsi_ip = {}
if len(self.configuration.hp3par_iscsi_ips) > 0:
for ip_addr in self.configuration.hp3par_iscsi_ips:
if self.configuration.iscsi_ip_address not in temp_iscsi_ip:
ip = ip_addr.split(':')
ip = self.configuration.iscsi_ip_address
iscsi_ports = self.common.get_ports()['iSCSI']
if len(ip) == 1:
ip_port = self.configuration.iscsi_port
for ip, iscsi_info in iscsi_ports.iteritems():
temp_iscsi_ip[ip_addr] = {'ip_port': DEFAULT_ISCSI_PORT}
if len(ip) == 2:
temp_iscsi_ip[ip] = {'ip_port': ip_port}
if ip in temp_iscsi_ip:
if self.configuration.iscsi_ip_address in temp_iscsi_ip:
temp_iscsi_ip[ip[0]] = {'ip_port': ip[1]}
msg = _("Invalid IP address format '%s'") % ip_addr
ip_port = temp_iscsi_ip[ip]['ip_port']
if len(temp_iscsi_ip) > 0:
LOG.warn(msg)
self.iscsi_ips[ip] = {'ip_port': ip_port, 'nsp': iscsi_info['nsp'], 'iqn':
    iscsi_info['iqn']}
msg = _(
    "Found invalid iSCSI IP address(s) in configuration option(s) hp3par_iscsi_ips or iscsi_ip_address '%s.'"
    ) % ', '.join(temp_iscsi_ip)
if not len(self.iscsi_ips) > 0:
LOG.warn(msg)
msg = _('At least one valid iSCSI IP address must be set.')
self.common.do_setup(context)
