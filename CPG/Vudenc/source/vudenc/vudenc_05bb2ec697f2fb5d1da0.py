def get_transform(self, name):...
transform = super().get_transform(name)
if transform:
return transform
if '_' not in name:
index = int(name)
index += 1
start, end = name.split('_')
return SliceTransformFactory(start, end)
return IndexTransformFactory(index, self.base_field)
start = int(start) + 1
end = int(end)
