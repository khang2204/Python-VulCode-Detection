def __init__(self, head, body):...
self.__class__.count += 1
self.__class__.todo.append(self)
from beamr.interpreters import Config
lettr = ''
num = self.__class__.count
while num:
lettr += chr(64 + num % 27)
self.insertCmd = Config.get('vbtmCmds', 'insertion')(lettr)
num //= 27
self.head = head
self.body = body
super(VerbatimEnv, self).__init__(self.insertCmd)
