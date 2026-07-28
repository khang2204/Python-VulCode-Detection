def _cliq_get_cluster_vip(self, cluster_name):...
"""docstring"""
cluster_xml = self._cliq_get_cluster_info(cluster_name)
vips = []
for vip in cluster_xml.findall('response/cluster/vip'):
vips.append(vip.attrib.get('ipAddress'))
if len(vips) == 1:
return vips[0]
_xml = etree.tostring(cluster_xml)
msg = _(
    'Unexpected number of virtual ips for cluster  %(cluster_name)s. Result=%(_xml)s'
    ) % {'cluster_name': cluster_name, '_xml': _xml}
