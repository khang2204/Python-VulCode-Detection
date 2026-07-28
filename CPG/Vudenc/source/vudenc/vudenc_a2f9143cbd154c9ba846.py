async def _runon(self, method):...
controller = self.controller
for b in controller._enabledBehavior:
f = getattr(b, 'on' + method)
await controller.processItem(item)
