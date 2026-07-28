"""Simple Markdown browser for a Git checkout."""
from __future__ import print_function
import SimpleHTTPServer
import SocketServer
import argparse
import codecs
import os
import re
import socket
import sys
import threading
import time
import webbrowser
from xml.etree import ElementTree
THIS_DIR = os.path.realpath(os.path.dirname(__file__))
SRC_DIR = os.path.dirname(os.path.dirname(THIS_DIR))
sys.path.insert(0, os.path.join(SRC_DIR, 'third_party', 'Python-Markdown'))
import markdown
def main(argv):...
parser = argparse.ArgumentParser(prog='md_browser')
parser.add_argument('-p', '--port', type=int, default=8080, help=
    'port to run on (default = %(default)s)')
parser.add_argument('-d', '--directory', type=str, default=SRC_DIR)
parser.add_argument('-e', '--external', action='store_true', help=
    'whether to bind to external port')
parser.add_argument('file', nargs='?', help='open file in browser')
args = parser.parse_args(argv)
top_level = os.path.realpath(args.directory)
hostname = '0.0.0.0' if args.external else 'localhost'
server_address = hostname, args.port
s = Server(server_address, top_level)
origin = 'http://' + hostname
if args.port != 80:
origin += ':%s' % args.port
print('Listening on %s/' % origin)
thread = None
if args.file:
path = os.path.realpath(args.file)
if os.path.isfile(os.path.join(top_level, 'docs', 'README.md')):
if not path.startswith(top_level):
print(' Try loading %s/docs/README.md' % origin)
if os.path.isfile(os.path.join(args.directory, 'README.md')):
print('%s is not under %s' % (args.file, args.directory))
rpath = os.path.relpath(path, top_level)
retcode = 1
print(' Try loading %s/README.md' % origin)
return 1
url = '%s/%s' % (origin, rpath)
s.serve_forever()
retcode = 130
s.shutdown()
print('Opening %s' % url)
print('Exception raised: %s' % str(e))
if thread:
thread = threading.Thread(target=_open_url, args=(url,))
thread.join()
return retcode
thread.start()
