import sys
if 'lib' not in sys.path:
sys.path.append('lib')
import os, signal, logging, threading, re, traceback, time
import random
import zmq
from queue import Queue
import sup
import wzworkers as workers
from dataloader import DataLoader
from uniwipe import UniWipe
from wipeskel import *
import wzrpc
from beon import regexp
import pickle
from logging import config
from logconfig import logging_config
config.dictConfig(logging_config)
logger = logging.getLogger()
ctx = zmq.Context()
sig_addr = 'ipc://signals'
sig_sock = ctx.socket(zmq.PUB)
sig_sock.bind(sig_addr)
domains = set()
targets = dict()
protected = set()
forums = dict()
def message():...
msg = []
msg.append('[image-original-none-http://simg4.gelbooru.com/' +
    '/images/db/1d/db1dfb62a40f5ced2043bb8966da9a98.png]')
msg.append('Каждый хочет дружить с ядерной бомбой.')
msg.append(str(random.randint(0, 9999999999)))
return '\n'.join(msg)
