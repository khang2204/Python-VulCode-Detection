def start_component(self, comp):...
node = self.nodes.get(comp['name'])
res = []
unres = []
dep_resolve(node, res, unres)
for node in res:
self.logger.debug("node name '%s' vs. comp name '%s'" % (node.comp_name,
    comp['name']))
self.logger.debug("All dependencies satisfied, starting '%s'" % comp['name'])
if node.comp_name != comp['name']:
state = self.check_component(node.component)
self.logger.debug('Checking and starting %s' % node.comp_name)
if state is CheckState.STARTED_BY_HAND or state is CheckState.RUNNING:
state = self.check_component(node.component)
self.logger.debug('Component %s is already running. Skipping start' % comp[
    'name'])
self.start_component_without_deps(comp)
if state is CheckState.STOPPED_BUT_SUCCESSFUL or state is CheckState.STARTED_BY_HAND or state is CheckState.RUNNING:
return True
self.logger.debug(
    'Component %s is already running, skipping to next in line' % comp['name'])
self.logger.debug("Start component '%s' as dependency of '%s'" % (node.
    comp_name, comp['name']))
self.start_component_without_deps(node.component)
tries = 0
while True:
self.logger.debug('Checking %s resulted in checkstate %s' % (node.comp_name,
    state))
state = self.check_component(node.component)
if state is not CheckState.RUNNING or state is not CheckState.STOPPED_BUT_SUCCESSFUL:
if tries > 100:
return False
tries = tries + 1
sleep(0.5)
