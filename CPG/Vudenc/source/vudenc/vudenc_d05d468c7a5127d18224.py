def _load_supported_hosts(self):...
"""docstring"""
import soscollector.hosts
package = soscollector.hosts
supported_hosts = {}
hosts = self._load_modules(package, 'hosts')
for host in hosts:
supported_hosts[host[0]] = host[1]
return supported_hosts
