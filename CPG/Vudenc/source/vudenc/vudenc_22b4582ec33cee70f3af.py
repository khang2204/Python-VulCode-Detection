import os
import sys
import socket
import string
import time
import urllib2
import HTMLParser
import zlib
import libirc
HOST = 'irc.freenode.net'
PORT = 6667
NICK = 'titlebot'
IDENT = 'titlebot'
REALNAME = 'titlebot'
CHANS = ['##Orz']
def ParseURL(s):...
http_idx = s.find('http:')
https_idx = s.find('https:')
if https_idx == -1:
if http_idx == -1:
if http_idx == -1:
return None
return s[http_idx:]
return s[https_idx:]
return s[min(http_idx, https_idx):]
