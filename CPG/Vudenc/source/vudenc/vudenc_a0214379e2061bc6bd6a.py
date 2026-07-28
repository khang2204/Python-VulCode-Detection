def __eq__(self, other):...
if other:
return vars(self) == vars(other)
return False
