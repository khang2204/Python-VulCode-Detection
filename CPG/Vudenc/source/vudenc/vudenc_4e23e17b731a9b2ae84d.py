def draw(self):...
drawings = []
for ID in self.actors.keys():
drawings = drawings + self.actors[ID].draw()
return drawings
