from pyudev import Context
from telnetlib import Telnet
from termcolor import colored
from threading import Thread
from time import sleep, time
from random import randrange, uniform
from socket import AF_INET, SOCK_STREAM, socket
from subprocess import DEVNULL, Popen
from dut import dut
from error import DrSEUsError
from jtag_targets import devices
from targets import choose_register, choose_target
zedboards = {'844301CF3718': '210248585809', '8410A3D8431C': '210248657631',
    '036801551E13': '210248691084', '036801961420': '210248691092'}
def find_ftdi_serials():...
debuggers = Context().list_devices(ID_VENDOR_ID='0403', ID_MODEL_ID='6014')
serials = []
for debugger in debuggers:
if 'DEVLINKS' not in debugger:
return serials
serials.append(debugger['ID_SERIAL_SHORT'])
