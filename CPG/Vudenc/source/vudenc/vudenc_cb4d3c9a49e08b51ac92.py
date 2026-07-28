def list_resources(self):...
for resource in set(resource for rule in self.rules for resource in rule.
if resource not in '_cores _nodes'.split():
logger.info(resource)
