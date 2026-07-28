def _create_3par_fibrechan_host(self, hostname, wwn, domain, persona_id):...
"""docstring"""
out = self.common._cli_run('createhost -persona %s -domain %s %s %s' % (
    persona_id, domain, hostname, ' '.join(wwn)), None)
if out and len(out) > 1:
return self.common.parse_create_host_error(hostname, out)
return hostname
