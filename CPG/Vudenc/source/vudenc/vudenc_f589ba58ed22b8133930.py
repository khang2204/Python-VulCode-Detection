from paramiko import AutoAddPolicy, SSHClient
from scp import SCPClient
from serial import Serial
import sys
from termcolor import colored
from time import sleep
from error import DrSEUsError
from sql import sql
error_messages = [('drseus_sighandler: SIGSEGV', 'Signal SIGSEGV'), (
    'drseus_sighandler: SIGILL', 'Signal SIGILL'), (
    'drseus_sighandler: SIGBUS', 'Signal SIGBUS'), (
    'drseus_sighandler: SIGFPE', 'Signal SIGFPE'), (
    'drseus_sighandler: SIGABRT', 'Signal SIGABRT'), (
    'drseus_sighandler: SIGIOT', 'Signal SIGIOT'), (
    'drseus_sighandler: SIGTRAP', 'Signal SIGTRAP'), (
    'drseus_sighandler: SIGSYS', 'Signal SIGSYS'), (
    'drseus_sighandler: SIGEMT', 'Signal SIGEMT'), ('command not found',
    'Invalid command'), ('No such file or directory', 'Missing file'), (
    'panic', 'Kernel error'), ('Oops', 'Kernel error'), (
    'Segmentation fault', 'Segmentation fault'), ('Illegal instruction',
    'Illegal instruction'), ('Call Trace:', 'Kernel error'), (
    'detected stalls on CPU', 'Stall detected'), (
    'malloc(), memory corruption', 'Kernel error'), ('Bad swap file entry',
    'Kernel error'), ('Unable to handle kernel paging request',
    'Kernel error'), ('Alignment trap', 'Kernel error'), ('Unhandled fault',
    'Kernel error'), ('free(), invalid next size', 'Kernel error'), (
    'double free or corruption', 'Kernel error'), ('????????', '????????'),
    ('Hit any key to stop autoboot:', 'Reboot'), ("can't get kernel image",
    'Error booting')]
def __init__(self, campaign_data, result_data, options, rsakey, aux=False):...
self.campaign_data = campaign_data
self.result_data = result_data
self.options = options
self.aux = aux
self.uboot_command = (self.options.dut_uboot if not self.aux else self.
    options.aux_uboot)
serial_port = options.dut_serial_port if not aux else options.aux_serial_port
baud_rate = options.dut_baud_rate if not aux else options.aux_baud_rate
self.serial = Serial(port=None, baudrate=baud_rate, timeout=options.timeout,
    rtscts=True)
if self.campaign_data['use_simics']:
self.serial._dsrdtr = True
self.serial.port = serial_port
self.serial.open()
self.serial.reset_input_buffer()
self.prompt = options.dut_prompt if not aux else options.aux_prompt
self.prompt += ' '
self.rsakey = rsakey
def __str__(self):...
string = 'Serial Port: ' + self.serial.port + '\n\tTimeout: ' + str(self.
    serial.timeout) + """ seconds
	Prompt: \"""" + self.prompt + '"'
string += '\n\tIP Address: ' + self.ip_address
string += '\n\tSCP Port: ' + str(self.options.dut_scp_port if not self.aux else
    self.options.aux_scp_port)
return string
