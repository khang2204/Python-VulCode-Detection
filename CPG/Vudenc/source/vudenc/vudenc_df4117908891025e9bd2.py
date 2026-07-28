def _create_3par_iscsi_host(self, hostname, iscsi_iqn, domain, persona_id):...
"""docstring"""
cmd = 'createhost -iscsi -persona %s -domain %s %s %s' % (persona_id,
    domain, hostname, iscsi_iqn)
out = self.common._cli_run(cmd, None)
if out and len(out) > 1:
return self.common.parse_create_host_error(hostname, out)
return hostname
