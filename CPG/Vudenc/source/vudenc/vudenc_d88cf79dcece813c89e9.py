def lineReceived(self, line):...
line = line.strip()
command, cmd_args = self.parse_line(line)
self.terminal.write('Syntax error: %s\n' % e.message)
deferred = defer.maybeDeferred(command, *cmd_args)
self.print_prompt()
@deferred...
return
self.print_prompt()
@deferred...
if not f.check(cmdline.ArgumentParsingError):
f.raiseException()
self.print_prompt()
ret = defer.Deferred()
deferred.addBoth(ret.callback)
return ret
