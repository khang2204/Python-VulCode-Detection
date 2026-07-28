import sublime
import sublime_plugin
import os
import re
import Urtext.datestimes
import Urtext.meta
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
from anytree import Node, RenderTree
import codecs
import logging
def get_path(window):...
"""docstring"""
if window.project_data():
path = window.project_data()['urtext_path']
path = '.'
return path
