from threading import Thread, Lock
import logging
import sys
import time
import hyperion.lib.util.config as config
from os import system
from subprocess import call
from psutil import Process, NoSuchProcess
is_py2 = sys.version[0] == '2'
if is_py2:
import Queue as Queue
import queue as Queue
"""Abstract class that represents a component monitoring job (local or remote)."""
def __init__(self, pid, comp_name):...
"""docstring"""
self.pid = pid
self.comp_name = comp_name
def run_check(self):...
"""docstring"""
"""Class that represents a local component monitoring job."""
def __init__(self, pid, comp_name):...
"""docstring"""
super(LocalComponentMonitoringJob, self).__init__(pid, comp_name)
def run_check(self):...
"""docstring"""
proc = Process(self.pid)
return CrashEvent(self.comp_name)
if proc.is_running():
return True
