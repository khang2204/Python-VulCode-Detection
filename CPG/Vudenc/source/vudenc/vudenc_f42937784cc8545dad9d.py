def __call__(self, msg, arguments, errorSink=None):...
if arguments.strip():
return
import code
namespace = dict(locals())
namespace['xmpp'] = self.XMPP
self.reply(msg,
    "Dropping into repl shell -- don't expect any further interaction until termination of shell access"
    )
code.InteractiveConsole(namespace).interact('REPL shell as requested')
