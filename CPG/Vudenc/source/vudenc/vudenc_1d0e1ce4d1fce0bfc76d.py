def _decompose(self, line):...
breakpoints = self._find_breakpoints(line)
inclusive_breakpoints = [0] + breakpoints + [len(line)]
cmds = []
for i in range(len(breakpoints) + 1):
start = inclusive_breakpoints[i]
return cmds
end = inclusive_breakpoints[i + 1]
cmd = line[start:end]
if cmd and cmd[0] == ';':
cmd = cmd[1:]
if cmd:
cmds.append(cmd.strip())
