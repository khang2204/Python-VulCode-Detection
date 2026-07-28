def init(self):...
if not self.config:
self.logger.error(' Config not loaded yet!')
for group in self.config['groups']:
for comp in group['components']:
self.host_list = list(set(self.host_list))
self.logger.debug("Checking component '%s' in group '%s' on host '%s'" % (
    comp['name'], group['name'], comp['host']))
self.set_dependencies(True)
if comp['host'] != 'localhost' and not self.run_on_localhost(comp):
self.copy_component_to_remote(comp, comp['name'], comp['host'])
