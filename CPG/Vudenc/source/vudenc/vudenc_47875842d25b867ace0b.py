"""Provides an argument parser and a set of default command line options for
using the ParlAI package.
"""
import argparse
import importlib
import os
import sys
from parlai.core.agents import get_agent_module, get_task_module
from parlai.tasks.tasks import ids_to_tasks
def str2bool(value):...
v = value.lower()
if v in ('yes', 'true', 't', '1', 'y'):
return True
if v in ('no', 'false', 'f', 'n', '0'):
return False
def str2class(value):...
"""docstring"""
if ':' not in value:
name = value.split(':')
module = importlib.import_module(name[0])
return getattr(module, name[1])
