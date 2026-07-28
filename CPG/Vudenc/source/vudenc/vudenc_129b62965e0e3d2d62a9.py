def banner():...
import socket
import getpass
return '%s in %s on %s' % (ansi.foreground(ansi.GREEN, env.project), ansi.
    foreground(env.color, env.name), ansi.foreground(ansi.CYAN, getpass.
    getuser() + '@' + socket.gethostname()))
