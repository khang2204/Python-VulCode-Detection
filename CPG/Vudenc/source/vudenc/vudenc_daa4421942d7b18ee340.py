def precmd(self, line):...
cmds = self._decompose(line)
if len(cmds) > 1:
self.cmdqueue.extend(cmds[1:])
return cmds[0]
