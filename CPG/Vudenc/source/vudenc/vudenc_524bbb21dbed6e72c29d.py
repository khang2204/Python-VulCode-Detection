def __init__(self, base_name, name, type):...
self.base_name = base_name
self.name = name
self.type = type
self.flattened = '{}.{}'.format(self.base_name, self.name
    ) if self.base_name else self.name
self.escaped = escape_col(self.flattened)
