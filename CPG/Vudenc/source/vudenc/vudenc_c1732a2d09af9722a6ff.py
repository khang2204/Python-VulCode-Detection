def properties(self, omit_resources='_cores _nodes'.split()):...
resources = {name: res for name, res in self.resources.items() if name not in
    omit_resources}
params = {name: value for name, value in self.params.items()}
properties = {'rule': self.rule.name, 'local': self.dag.workflow.is_local(
    self.rule), 'input': self.input, 'output': self.output, 'params':
    params, 'threads': self.threads, 'resources': resources}
return properties
