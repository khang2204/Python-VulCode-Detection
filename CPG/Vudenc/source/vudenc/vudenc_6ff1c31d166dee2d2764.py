def user_tree(self, uname, readable=False, writable=False):...
ret = []
opt1 = readable and uname in self.uread
opt2 = writable and uname in self.uwrite
if opt1 or opt2:
ret.append(self.vpath)
for _, vn in sorted(self.nodes.items()):
ret.extend(vn.user_tree(uname, readable, writable))
return ret
