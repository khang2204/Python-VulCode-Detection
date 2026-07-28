def __str__(self):...
s = self.before
for c in self.children:
s += str(c) + self.inter
s += self.after
return s
