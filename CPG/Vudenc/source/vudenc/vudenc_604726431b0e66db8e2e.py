from difflib import SequenceMatcher
import os
from paramiko import RSAKey
from shutil import copy, rmtree
from subprocess import PIPE, Popen
from termcolor import colored
from threading import Thread
from time import sleep
from error import DrSEUsError
from jtag import bdi_p2020, openocd
from simics import simics
from sql import sql
def __init__(self, campaign_data, options):...
self.campaign_data = campaign_data
self.options = options
self.result_data = {'campaign_id': self.campaign_data['id'], 'aux_output':
    '', 'data_diff': None, 'debugger_output': '', 'detected_errors': None,
    'dut_output': ''}
if os.path.exists('campaign-data/' + str(campaign_data['id']) + '/private.key'
self.rsakey = RSAKey.from_private_key_file('campaign-data/' + str(
    campaign_data['id']) + '/private.key')
self.rsakey = RSAKey.generate(1024)
if self.campaign_data['use_simics']:
self.rsakey.write_private_key_file('campaign-data/' + str(campaign_data[
    'id']) + '/private.key')
self.debugger = simics(campaign_data, self.result_data, options, self.rsakey)
if campaign_data['architecture'] == 'p2020':
if not self.campaign_data['use_simics']:
self.debugger = bdi_p2020(campaign_data, self.result_data, options, self.rsakey
    )
if campaign_data['architecture'] == 'a9':
if self.campaign_data['use_aux']:
def __str__(self):...
self.debugger = openocd(campaign_data, self.result_data, options, self.rsakey)
self.debugger.aux.serial.write('\x03')
if options.command == 'new':
string = """DrSEUs Attributes:
	Debugger: """ + str(self.debugger
    ) + '\n\tDUT:\t' + str(self.debugger.dut).replace('\n\t', '\n\t\t')
self.debugger.aux.do_login()
self.debugger.reset_dut()
if self.campaign_data['use_aux']:
if options.command != 'new':
string += '\n\tAUX:\t' + str(self.debugger.aux).replace('\n\t', '\n\t\t')
string += """
	Campaign Information:
		Campaign Number: """ + str(self.
    campaign_data['id']) + """
		DUT Command: \"""" + self.campaign_data[
    'command'] + '"'
self.send_dut_files(aux=True)
if self.campaign_data['use_aux']:
string += """
		AUX Command: \"""" + self.campaign_data['aux_command'] + '"'
string += '\n\t\t' + ('Host ' if self.campaign_data['use_simics'] else ''
    ) + 'Execution Time: ' + str(self.campaign_data['exec_time']) + ' seconds'
if self.campaign_data['use_simics']:
string += """
		Execution Cycles: """ + '{:,}'.format(self.campaign_data[
    'num_cycles']) + """ cycles
		Simulated Time: """ + str(self.
    campaign_data['sim_time']) + ' seconds'
return string
