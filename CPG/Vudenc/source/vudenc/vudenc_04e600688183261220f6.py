def addActor(self, actor):...
self.ids += 1
self.actors[self.ids] = actor
self.actors[self.ids].bound(self.max_x, self.max_y)
return self.ids
