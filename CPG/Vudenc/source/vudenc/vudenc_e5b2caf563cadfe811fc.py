def __init__(self, obj, readonly=False):...
self.id = random_id(obj.get('id'))
self.name = obj['name']
self.category = obj.get('category', 'Misc')
self.program = obj['program']
self.arguments = obj.get('arguments', [])
self.readonly = readonly
self.ui_properties = obj.get('ui_properties', None)
