from libtmux import Server
from yaml import load, dump
from setupParser import Loader
from DepTree import Node, dep_resolve, CircularReferenceException
import logging
import os
import socket
import argparse
from psutil import Process
from subprocess import call
from graphviz import Digraph
from enum import Enum
from time import sleep
import sys
from PyQt4 import QtGui
import hyperGUI
FORMAT = '%(asctime)s: %(name)s [%(levelname)s]:\t%(message)s'
logging.basicConfig(level=logging.WARNING, format=FORMAT, datefmt='%I:%M:%S')
TMP_SLAVE_DIR = '/tmp/Hyperion/slave/components'
TMP_COMP_DIR = '/tmp/Hyperion/components'
TMP_LOG_PATH = '/tmp/Hyperion/log'
BASE_DIR = os.path.dirname(__file__)
SCRIPT_CLONE_PATH = '%s/scripts/start_named_clone_session.sh' % BASE_DIR
RUNNING = 0
STOPPED = 1
STOPPED_BUT_SUCCESSFUL = 2
STARTED_BY_HAND = 3
DEP_FAILED = 4
def __init__(self, configfile=None):...
self.logger = logging.getLogger(__name__)
self.logger.setLevel(logging.DEBUG)
self.configfile = configfile
self.nodes = {}
self.server = []
self.host_list = []
if configfile:
self.load_config(configfile)
self.config = None
self.session_name = self.config['name']
def load_config(self, filename='default.yaml'):...
dump(self.config, outfile, default_flow_style=False)
self.config = load(data_file, Loader)
self.logger.debug('Loading config was successful')
def init(self):...
self.server = Server()
if not self.config:
if self.server.has_session(self.session_name):
self.logger.error(' Config not loaded yet!')
for group in self.config['groups']:
self.session = self.server.find_where({'session_name': self.session_name})
self.logger.info('starting new session by name "%s" on server' % self.
    session_name)
def set_dependencies(self, exit_on_fail):...
for comp in group['components']:
self.host_list = list(set(self.host_list))
self.logger.info('found running session by name "%s" on server' % self.
    session_name)
self.session = self.server.new_session(session_name=self.session_name,
    window_name='Main')
for group in self.config['groups']:
self.logger.debug("Checking component '%s' in group '%s' on host '%s'" % (
    comp['name'], group['name'], comp['host']))
self.set_dependencies(True)
for comp in group['components']:
master_node = Node({'name': 'master_node'})
if comp['host'] != 'localhost' and not self.run_on_localhost(comp):
self.nodes[comp['name']] = Node(comp)
for name in self.nodes:
self.copy_component_to_remote(comp, comp['name'], comp['host'])
node = self.nodes.get(name)
self.nodes['master_node'] = master_node
master_node.addEdge(node)
node = self.nodes.get('master_node')
self.logger.error(
    'Detected circular dependency reference between %s and %s!' % (ex.node1,
    ex.node2))
def copy_component_to_remote(self, infile, comp, host):...
if 'depends' in node.component:
res = []
if exit_on_fail:
self.host_list.append(host)
for dep in node.component['depends']:
unres = []
exit(1)
self.logger.debug('Saving component to tmp')
if dep in self.nodes:
dep_resolve(node, res, unres)
tmp_comp_path = '%s/%s.yaml' % (TMP_COMP_DIR, comp)
node.addEdge(self.nodes[dep])
self.logger.error("Unmet dependency: '%s' for component '%s'!" % (dep, node
    .comp_name))
dep_string = ''
ensure_dir(tmp_comp_path)
if exit_on_fail:
for node in res:
dump(infile, outfile, default_flow_style=False)
exit(1)
if node is not master_node:
self.logger.debug('Dependency tree for start all: %s' % dep_string)
self.logger.debug('Copying component "%s" to remote host "%s"' % (comp, host))
dep_string = '%s -> %s' % (dep_string, node.comp_name)
cmd = "ssh %s 'mkdir -p %s' & scp %s %s:%s/%s.yaml" % (host, TMP_SLAVE_DIR,
    tmp_comp_path, host, TMP_SLAVE_DIR, comp)
self.logger.debug(cmd)
send_main_session_command(self.session, cmd)
def stop_component(self, comp):...
if comp['host'] != 'localhost' and not self.run_on_localhost(comp):
self.logger.debug("Stopping remote component '%s' on host '%s'" % (comp[
    'name'], comp['host']))
window = find_window(self.session, comp['name'])
self.stop_remote_component(comp['name'], comp['host'])
if window:
def stop_remote_component(self, comp_name, host):...
self.logger.debug("window '%s' found running" % comp['name'])
cmd = "ssh %s 'hyperion --config %s/%s.yaml slave --kill'" % (host,
    TMP_SLAVE_DIR, comp_name)
self.logger.info('Shutting down window...')
self.logger.debug('Run cmd:\n%s' % cmd)
kill_window(window)
send_main_session_command(self.session, cmd)
self.logger.info('... done!')
def start_component(self, comp):...
node = self.nodes.get(comp['name'])
res = []
unres = []
dep_resolve(node, res, unres)
for node in res:
self.logger.debug("node name '%s' vs. comp name '%s'" % (node.comp_name,
    comp['name']))
self.logger.debug("All dependencies satisfied, starting '%s'" % comp['name'])
if node.comp_name != comp['name']:
state = self.check_component(node.component)
self.logger.debug('Checking and starting %s' % node.comp_name)
if state is CheckState.STARTED_BY_HAND or state is CheckState.RUNNING:
state = self.check_component(node.component)
self.logger.debug('Component %s is already running. Skipping start' % comp[
    'name'])
self.start_component_without_deps(comp)
if state is CheckState.STOPPED_BUT_SUCCESSFUL or state is CheckState.STARTED_BY_HAND or state is CheckState.RUNNING:
return True
self.logger.debug(
    'Component %s is already running, skipping to next in line' % comp['name'])
self.logger.debug("Start component '%s' as dependency of '%s'" % (node.
    comp_name, comp['name']))
self.start_component_without_deps(node.component)
tries = 0
while True:
self.logger.debug('Checking %s resulted in checkstate %s' % (node.comp_name,
    state))
state = self.check_component(node.component)
if state is not CheckState.RUNNING or state is not CheckState.STOPPED_BUT_SUCCESSFUL:
if tries > 100:
return False
tries = tries + 1
sleep(0.5)
