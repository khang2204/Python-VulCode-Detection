import os
from columnize import columnize
from twisted.internet import defer
from opennode.oms.endpoint.ssh import cmd, completion, cmdline
from opennode.oms.endpoint.ssh.terminal import InteractiveTerminal
from opennode.oms.endpoint.ssh.tokenizer import CommandLineTokenizer, CommandLineSyntaxError
from opennode.oms.zodb import db
"""The OMS virtual console over SSH.

    Accepts lines of input and writes them back to its connection.  If
    a line consisting solely of "quit" is received, the connection
    is dropped.

    """
def __init__(self):...
super(OmsSshProtocol, self).__init__()
self.path = ['']
@defer.inlineCallbacks...
self.obj_path = yield db.transact(lambda : [db.ref(db.get_root()['oms_root'])]
    )()
_get_obj_path()
self.tokenizer = CommandLineTokenizer()
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
