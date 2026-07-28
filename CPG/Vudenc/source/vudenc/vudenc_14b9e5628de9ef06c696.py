def __init__(self):...
self.content = None
self.filled = False
def set(self, content):...
if content == 'L':
self.content = 'L'
if content == 'R':
self.filled = True
self.content = 'R'
self.content = content
def get(self):...
self.filled = True
return self.content
