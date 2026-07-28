def _create_host(self, volume, connector):...
"""docstring"""
host = None
hostname = self.common._safe_hostname(connector['host'])
cpg = self.common.get_cpg(volume, allowSnap=True)
domain = self.common.get_domain(cpg)
host = self.common._get_3par_host(hostname)
persona_id = self.common.get_persona_type(volume)
return host
if not host['FCPaths']:
hostname = self._create_3par_fibrechan_host(hostname, connector['wwpns'],
    domain, persona_id)
self._modify_3par_fibrechan_host(hostname, connector['wwpns'])
host = self.common._get_3par_host(hostname)
host = self.common._get_3par_host(hostname)
