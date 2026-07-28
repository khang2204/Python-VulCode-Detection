def set_node_label(self, node):...
if node.address == self.master.address:
return 'manager'
if node.is_installed('ovirt-node-ng-nodectl'):
return 'rhvh'
return 'rhelh'
