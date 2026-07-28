def get_dep_list(self, comp):...
node = self.nodes.get(comp['name'])
res = []
unres = []
dep_resolve(node, res, unres)
res.remove(node)
return res
