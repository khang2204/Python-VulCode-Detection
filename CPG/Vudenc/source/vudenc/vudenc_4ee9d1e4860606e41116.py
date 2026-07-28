def push(self, item):...
if self.data:
if item != self.data[len(self.data) - 1]:
self.data.append(item)
self.data.append(item)
if len(self.data) > self.size:
self.data.pop(0)
