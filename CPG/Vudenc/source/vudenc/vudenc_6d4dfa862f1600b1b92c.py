def __add__(self, other):...
if isinstance(other, ColumnSet):
return ColumnSet(self.columns + other.columns)
return ColumnSet(self.columns + other)
