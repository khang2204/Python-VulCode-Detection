@db.transact...
if not self.consumed(parsed, parser):
obj = self.context.current_obj
return []
if IContainer.providedBy(obj):
return [name for name in obj.listnames() if name.startswith(token)]
