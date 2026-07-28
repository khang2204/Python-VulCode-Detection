import socket
import sys
import re
import os
from _thread import *
from subprocess import Popen, PIPE
HOST = ''
PORT = 4949
VERSION = '0.1.0'
ENCODING = 'utf-8'
LINEBREAK = '\n'
PLUGINPATH = os.getcwd() + '\\plugins'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
print('failed!' + str(msg.errno))
s.listen(10)
sys.exit()
def output(what):...
return what.encode(ENCODING)
