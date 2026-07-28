def deconstruct(self):...
name, path, args, kwargs = super().deconstruct()
if self.default == '{}':
if self.encoder is not None:
kwargs['encoder'] = self.encoder
return name, path, args, kwargs
