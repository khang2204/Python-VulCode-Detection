"""
Beamr

@author:     Teodor Gherasim Nistor

@copyright:  2018 Teodor Gherasim Nistor

@license:    MIT License
"""
from __future__ import print_function
import sys
import beamr.debug as debug
from beamr import setup_arg, cli_name
from docopt import docopt
def main():...
halp = (
    """%s - %s

    Usage:
        %s [-n|-p <cmd>] [-q|-v] [-u|-s] [-c <cfg>] [--] [- | <input-file>] [- | <output-file>]
        %s (-h|-e [<editor>]) [-v]
        %s --version

    Options:
        -p <cmd>, --pdflatex=<cmd>  Specify pdflatex executable name and/or path to [default: pdflatex]
        -c <cfg>, --config=<cfg>    Override configuration. <cfg> must be valid Yaml
        -e, --edit-config     Open user configuration file for editing. An editor must be specified if configuration doesn't exist or doesn't mention one
        -n, --no-pdf   Don't create PDF output file (just generate Latex source)
        -u, --unsafe   Trust certain user input which cannot be verified
        -s, --safe     Don't trust user input which cannot be verified
        -v, --verbose  Print inner workings of the lexer-parser-interpreter cycle to stderr
        -q, --quiet    Print nothing except errors to stderr. If using Python >=3.6 this will also mute output from pdflatex
        -h, --help     Show this message and exit.
        --version      Print version information
"""
     % (setup_arg['name'], setup_arg['description'], cli_name, cli_name,
    cli_name))
arg = docopt(halp, version=setup_arg['version'])
if arg['--verbose']:
debug.verbose = True
if arg['--quiet']:
debug.quiet = True
debug.debug('args:', str(arg).replace('\n', ''))
from beamr.interpreters.config import Config
if arg['--edit-config']:
return Config.editUserConfig(arg['<editor>'])
pdflatex = None
if not arg['--no-pdf']:
pdflatex = [arg['--pdflatex'], '-shell-escape']
if arg['<input-file>']:
if arg['<output-file>']:
sys.stdin = open(arg['<input-file>'], 'r')
if arg['<output-file>']:
outFile = arg['<output-file>']
sys.stdout = open(arg['<output-file>'], 'w')
cmdlineSpecial = {}
arg['<output-file>'] = None
if arg['--safe']:
i = outFile.rfind('/') + 1
cmdlineSpecial['safe'] = True
if arg['--unsafe']:
if i > 0:
Config.fromCmdline(arg['--config'], **cmdlineSpecial)
cmdlineSpecial['safe'] = False
pdflatex.append('-output-directory=' + outFile[:i])
pdflatex.append('-jobname=' + outFile[i:])
from beamr.interpreters import Document
doc = Document(sys.stdin.read())
tex = str(doc)
if pdflatex:
from subprocess import Popen, PIPE
print(tex)
runkwarg = {'stdin': PIPE}
if __name__ == '__main__':
if debug.quiet:
sys.exit(main())
runkwarg.update({'stdout': PIPE, 'stderr': PIPE})
sp = Popen(pdflatex, **runkwarg)
sp.communicate(bytes(tex, encoding='utf-8'))
sp.communicate(bytes(tex))
sp.stdin.close()
rcode = sp.wait()
if rcode:
debug.err('Fatal: pdflatex exited with nonzero status', rcode)
return rcode
